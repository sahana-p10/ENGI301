# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Main Script to Display Time and Call Alarm 
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

from alarm_setting import *
from alarm_sound import *
from spi_screen import * 



# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

def main():
    alarm_clock = AlarmSetting()
    alarm_sound = AlarmSound()
    spi_screen = SPI_Display()
    
    while True:
        
        # Conditions if the set alarm button (black button) is pressed
        if alarm_clock.set_alarm_button.is_pressed():
            alarm_clock.toggle_alarm_mode()
    
        if alarm_clock.alarm_mode:
            if alarm_clock.hour_button.is_pressed(): # when the hour button is pressed
                alarm_clock.increase_alarm_hour()
            elif alarm_clock.min_button.is_pressed(): # when the minute button is pressed 
                alarm_clock.increase_alarm_minute()
        
        # Set time for checking alarm 
        current_time = time.localtime()
        alarm_hour = current_time.tm_hour
        alarm_minute = current_time.tm_min

        # Check if  alarm time set in AlarmClock matches the current time
        if alarm_clock.alarm_hour == alarm_hour and alarm_clock.alarm_minute == alarm_minute:
            # Play the alarm sounr
            alarm_sound.play_alarm_sound()

        # Update the alarm_clock time
        alarm_clock.display_alarm_time()
        


# ------------------------------------------------------------------------
# Main Script - Triggering alarm
# ------------------------------------------------------------------------

if __name__ == "__main__":
    main()
    
 