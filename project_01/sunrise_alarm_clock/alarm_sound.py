# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Setting Alarm Sound
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
import time

import Adafruit_BBIO.PWM as PWM

from buzzer_template import Buzzer
from button_template import Button



# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Main Tasks
# ------------------------------------------------------------------------


class AlarmSound:
    
    def __init__(self):
        # Create instances of the Buzzer and Button classes
        self.buzzer = Buzzer("P1_36")  # Actual GPIO pin
        self.stop_alarm_button = Button("P2_4")  # Actual GPIO pin

    def check_if_pressed(self): # checks to see if alarm stop button is pressed
        if self.stop_alarm_button.is_pressed():
            self.buzzer.cleanup()
            print("Alarm stopped")
            exit()
            
    def play_alarm_sound(self):
        
        buzzer = Buzzer("P1_36")  # Actual GPIO pin
        stop_alarm_button = Button("P2_4")  # Actual GPIO pin
    
        # Use buzzer instance to play tones
        print("Press button to stop the alarm")
        
        # Setting up alarm loop 
        
        # while loop 
        while stop_alarm_button.wait_for_press:
            
            # playing Viva la Vida by Coldplay (good wake up sound)
        
            # C5 ----------------------- 
            buzzer.play(523.25, 0.3, False) 
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
    
    
            buzzer.play(523.25, 0.3, False) 
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(523.25, 0.3, False) 
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(523.25, 0.25, False) 
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
        
            # D5 ---------------------------
            buzzer.play(587.33, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(587.33, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(587.33, 0.25, False)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(587.33, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(587.33, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            
            # B4 -------------------------------
            buzzer.play(493.88, 0.3, False)  
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(493.88, 0.3, False)  
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(493.88, 0.3, False)  
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(493.88, 0.25, False) 
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            # D5 -------------------------------
            buzzer.play(659.25, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(659.25, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(659.25, 0.25, False)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(659.25, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(659.25, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            # C5 ----------------------- 
            buzzer.play(523.25, 0.3, False) 
            time.sleep(0.2)
            
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
    
    
            buzzer.play(523.25, 0.3, False) 
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(523.25, 0.3, False) 
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(523.25, 0.25, False) 
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
        
            # D5 ---------------------------
            buzzer.play(587.33, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(587.33, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(587.33, 0.25, False)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(587.33, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(587.33, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            
            # B4 -------------------------------
            buzzer.play(493.88, 0.3, False)  
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(493.88, 0.3, False)  
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(493.88, 0.3, False)  
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(493.88, 0.25, False) 
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            # C5 --------------------------
            buzzer.play(523.25, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(523.25, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(523.25, 0.25, False)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(523.25, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break
            
            buzzer.play(523.25, 0.3, False)
            time.sleep(0.2)
            # Check if button is pressed 
            if stop_alarm_button.is_pressed():
                buzzer.cleanup()
                print("Alarm stopped")
                break

        
                
    # end def 
    
# end class 

# ------------------------------------------------------------------------
# Main Script - Triggering and stopping alarm 
# ------------------------------------------------------------------------

if __name__ == '__main__': 
    
    
    buzzer = Buzzer("P1_36")  # Actual GPIO pin
    stop_alarm_button = Button("P2_4")  # Actual GPIO pin

    # Use buzzer instance to play tones
    print("Press button to stop the alarm")
    
    # Setting up alarm loop 
    
    # while loop 
    while stop_alarm_button.wait_for_press:
        
        # playing Viva la Vida by Coldplay (good wake up sound)
    
        # C5 ----------------------- 
        buzzer.play(523.25, 0.3, False) 
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break


        buzzer.play(523.25, 0.3, False) 
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(523.25, 0.3, False) 
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(523.25, 0.25, False) 
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
    
        # D5 ---------------------------
        buzzer.play(587.33, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(587.33, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(587.33, 0.25, False)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(587.33, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(587.33, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        
        # B4 -------------------------------
        buzzer.play(493.88, 0.3, False)  
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(493.88, 0.3, False)  
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(493.88, 0.3, False)  
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(493.88, 0.25, False) 
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        # D5 -------------------------------
        buzzer.play(659.25, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(659.25, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(659.25, 0.25, False)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(659.25, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(659.25, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        # C5 ----------------------- 
        buzzer.play(523.25, 0.3, False) 
        time.sleep(0.2)
        
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break


        buzzer.play(523.25, 0.3, False) 
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(523.25, 0.3, False) 
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(523.25, 0.25, False) 
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
    
        # D5 ---------------------------
        buzzer.play(587.33, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(587.33, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(587.33, 0.25, False)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(587.33, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(587.33, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        
        # B4 -------------------------------
        buzzer.play(493.88, 0.3, False)  
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(493.88, 0.3, False)  
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(493.88, 0.3, False)  
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(493.88, 0.25, False) 
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        # C5 --------------------------
        buzzer.play(523.25, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(523.25, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(523.25, 0.25, False)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(523.25, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        
        buzzer.play(523.25, 0.3, False)
        time.sleep(0.2)
        # Check if button is pressed 
        if stop_alarm_button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break

    
    
# ------------------------------------------------------------------------