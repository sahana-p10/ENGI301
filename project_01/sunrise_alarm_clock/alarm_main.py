# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Main Alarm Setting and Playing  
--------------------------------------------------------------------------
License:   
Copyright 2023 Sahana Prasanna


Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

"""
# Import the necessary libraries for SPI screen and button control
from button_template import Button
import time

# Import the Buzzer and SPI screen setup from the previous scripts
from buzzer_template import Buzzer
from spi_screen import *
from alarm_sound import *

from pytz import timezone
from datetime import datetime

# for LED lights 

import time
import subprocess
import threading
# Replace 'path_to_opc' with the absolute path to the 'opc' script on your system
path_to_opc = '/home/debian/.local/bin/opc'
import opc

ADDRESS = 'localhost:7890'

# Create a client object
client = opc.Client(ADDRESS)

# Test if it can connect
if client.can_connect():
    print ('connected to %s' % ADDRESS)
else:
    # We could exit here, but instead let's just print a warning
    # and then keep trying to send pixels in case the server
    # appears later
    print ('WARNING: could not connect to %s' % ADDRESS)



# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

class AlarmSetting:
    def __init__(self, buzzer_pin="P1_36", spi_screen=None):
        self.buzzer = Buzzer(buzzer_pin)
        self.spi_screen = spi_screen if spi_screen else SPI_Display()
        self.alarm_sound = AlarmSound()
        self.set_alarm_button = Button("P2_10")  # Black button for setting alarm
        self.hour_button = Button("P2_6")  # Green button for setting hour
        self.min_button = Button("P2_8")  # Blue button for setting min
        self.led_button = Button("P2_2") # Yellow button for turning off LED lights 
        self.alarm_hour = 0
        self.alarm_minute = 0
        self.alarm_mode = False
        
    def display_time(self):
        print("displaying time")
        while True:
            self.spi_screen.display_datetime(fontsize=36, time_fontsize=64, fontcolor=(255, 255, 255))
            time.sleep(15)  # Update time every 15 sec
    
    def display_alarm_time(self):
        alarm_time = f"Alarm: {self.alarm_hour:02}:{self.alarm_minute:02}"
        self.spi_screen.fill((0, 0, 0))  # Clear the screen
        self.spi_screen.text(alarm_time, fontsize=36, fontcolor=(255, 255, 255), justify=CENTER, align=CENTER)  # Display the time

    def set_alarm_mode(self):
        self.spi_screen.fill((0, 0, 0))  # Clear the screen
        self.spi_screen.text(["Alarm Mode"], fontsize=36, justify=CENTER, align=CENTER)  # Display the alarm mode

    def toggle_alarm_mode(self):
        print("Black button pressed - Alarm Mode")
        self.alarm_mode = not self.alarm_mode
        if self.alarm_mode:
            self.set_alarm_mode()
        else:
            self.display_alarm_time()

    def increase_alarm_hour(self):
        print("Green hour button pressed")
        self.alarm_hour = (self.alarm_hour + 1) % 24
        self.display_alarm_time()
        time.sleep(0.2)  # Debounce

    def increase_alarm_minute(self):
        print("Blue minute button pressed")
        self.alarm_minute = (self.alarm_minute + 5) % 60
        self.display_alarm_time()
        time.sleep(0.2)  # Debounce

    def set_alarm(self, hour, minute):
        self.alarm_hour = hour
        self.alarm_minute = minute
        self.display_alarm_time()

    def trigger_alarm(self):
        # Add code to trigger the alarm using the buzzer when the desired time is reached
        pass
                    
    # Uses each light's address to set display to set a color - LED lights 
    def LED_strip_lights(self):
        
        # Define Pixel String
        global leds # declare leds as global variable 
        STR_LEN=9
        leds = []
        
        # define ending colors for each LED 
        
        colors = [
        
        # a fraction of the original RGB codes
            (102, 0, 0), # red
            (102, 26, 0), # orange
            (102,52,5), # yellow 
            (102,44,50), # pink
            (70,14,42), # purple
            (102,44,50), # pink
            (102,52,10), # yellow 
            (102, 26, 0), # orange
            (102, 0, 0), # red
            
         ]
 
        transition_time = 30  # adjust based on preference, at 5 minutes currently 
        step = 1  # Step size to increase brightness
        start_time = time.time()
        led_button = Button("P2_2") # Yellow button for turning off LED lights 
        led_off = False
        
        leds = [(0, 0, 0)] * STR_LEN
        
        while True:
            current_time = time.time() - start_time
            
            if led_button.is_pressed():
                # LED button is pressed, turn off the lights 
                print("Button pressed")
                led_off = True
                leds = [(0, 0, 0)] * STR_LEN  # Set all LEDs to off
                
            
            if not led_off:
                if current_time >= transition_time:
                    for i in range(STR_LEN):
                       
                        leds[i] = colors[i % len(colors)]  # Set LEDs to their final colors
                    if not client.put_pixels(leds, channel=0):
                        print('not connected')
                else:
                    brightness_progress = min(current_time / transition_time, 1.0)
                    for i in range(STR_LEN):
                        new_color = tuple(int(colors[i % len(colors)][j] * brightness_progress) for j in range(3))
                        if i < len(leds): 
                            leds[i] = new_color
    
    
            if not client.put_pixels(leds, channel=0):
                print('not connected')
                
            
            time.sleep(0.1)

# End def            
    
    # running everthing             
    def run(self):
        
        #start spi thread
        spi_thread = threading.Thread(target=self.display_time,daemon=True)
        spi_thread.start()
        
        while True:
           
            if self.set_alarm_button.is_pressed(): # setting alarm mode 
                print("Set alarm button pressed")
                self.toggle_alarm_mode()

            if self.alarm_mode:
                if self.hour_button.is_pressed(): # increasing hour 
                    self.increase_alarm_hour()
                elif self.min_button.is_pressed(): # increasing minute
                    self.increase_alarm_minute()
                elif self.set_alarm_button.is_pressed(): # going back to time 
                    self.display_time()
            
                
            central = timezone('US/Central')
            loc_dt = datetime.now(central)
            
            # checking to see if alarm time equals local time 
            alarm_hour = loc_dt.hour
            alarm_minute = loc_dt.minute
            alarm_second = loc_dt.second
    
            # implementing LED lights 
            if alarm_clock.alarm_minute == 0: 
                if alarm_clock.alarm_hour-1 == alarm_hour and alarm_clock.alarm_minute ==  55 and alarm_second == 0: 
                    # start the LED lights brightness increase 
                    # self.LED_strip_lights()
                    led_thread = threading.Thread(target=self.LED_strip_lights)
                    led_thread.start()
            elif alarm_clock.alarm_minute != 0:
                if alarm_clock.alarm_hour == alarm_hour and alarm_clock.alarm_minute-1 == alarm_minute and alarm_second == 0:
                    print("LED starts")
                    # start the LED lights brightness increase 
                    led_thread = threading.Thread(target=self.LED_strip_lights)
                    led_thread.start()
                    # self.LED_strip_lights()
        
            
            # if alarm time equals local time, play alarm sound 
            if alarm_clock.alarm_hour == alarm_hour and alarm_clock.alarm_minute == alarm_minute and alarm_second == 0:
                # Play the alarm sound
                self.alarm_sound.play_alarm_sound()
                
    
        
            time.sleep(0.1)  # Small delay to avoid excessive checking
        


# ------------------------------------------------------------------------
# Main Script - Setting Alarm
# ------------------------------------------------------------------------

if __name__ == "__main__":
    alarm_clock = AlarmSetting()
    alarm_clock.run()
    
# ------------------------------------------------------------------------