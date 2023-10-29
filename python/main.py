# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Main Class for Sunrise Alarm Clock
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

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Main Tasks
# ------------------------------------------------------------------------


# Import required classes 
from buzzer import Buzzer
from button import Button


# ------------------------------------------------------------------------
# Triggering and stopping alarm 
# ------------------------------------------------------------------------


if __name__ == '__main__': 
    buzzer = Buzzer("P2_1")  # replace P2_1 with your GPIO pin 
    
    # Use buzzer instance to play tones
    print("Press button to stop the alarm")
    
    # creating instance of Button class 
    button = Button("P2_2")  # Replace "P2_2" with the actual GPIO pin

    user_input = '' # user input for simulating button 

    # Setting up alarm loop 
    
    # while loop that should be changed to be time: 
    while user_input != 'q':
    
        # playing Viva la Vida by Coldplay (good wake up sound)
    
        # C5 
        buzzer.play(523.25, 0.5, False)  
        buzzer.play(523.25, 0.5, False) 
        buzzer.play(523.25, 0.5, False)
        buzzer.play(523.25, 0.25, False) 
        
        # D5 
        buzzer.play(587.33, 0.5, False)
        buzzer.play(587.33, 0.5, False)
        buzzer.play(587.33, 0.25, False)
        buzzer.play(587.33, 0.5, False)
        buzzer.play(587.33, 0.5, False)
        
        
        # B4 
        buzzer.play(493.88, 0.5, False)  
        buzzer.play(493.88, 0.5, False) 
        buzzer.play(493.88, 0.5, False)
        buzzer.play(493.88, 0.25, False) 
        
        # D5 
        buzzer.play(659.25, 0.5, False)
        buzzer.play(659.25, 0.5, False)
        buzzer.play(659.25, 0.25, False)
        buzzer.play(659.25, 0.5, False)
        buzzer.play(659.25, 0.5, False)
        
        # C5 
        buzzer.play(523.25, 0.5, False)  
        buzzer.play(523.25, 0.5, False) 
        buzzer.play(523.25, 0.5, False)
        buzzer.play(523.25, 0.25, False) 
        
        # D5 
        buzzer.play(587.33, 0.5, False)
        buzzer.play(587.33, 0.5, False)
        buzzer.play(587.33, 0.25, False)
        buzzer.play(587.33, 0.5, False)
        buzzer.play(587.33, 0.5, False)
        
        
        # B4 
        buzzer.play(493.88, 0.5, False)  
        buzzer.play(493.88, 0.5, False) 
        buzzer.play(493.88, 0.5, False)
        buzzer.play(493.88, 0.25, False) 
        
        # C5 
        buzzer.play(523.25, 0.5, False)
        buzzer.play(523.25, 0.5, False)
        buzzer.play(523.25, 0.25, False)
        buzzer.play(523.25, 0.5, False)
        buzzer.play(523.25, 0.5, False)
    

        # Check if button is pressed 
        """
        if button.is_pressed():
            buzzer.cleanup()
            print("Alarm stopped")
            break
        """
        
        # stimulating button press
        user_input = input()
        if user_input == 'q':
            buzzer.cleanup()
            print("Alarm stopped")
            break
    
    print("Test Complete")
    
    
# ------------------------------------------------------------------------