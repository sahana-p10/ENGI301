"""
--------------------------------------------------------------------------
LED Strip Light Test
--------------------------------------------------------------------------
License:   
Copyright 2021 Erik Welsh

Based on Code from:  https://github.com/rpliu3/ENGI301/tree/master/Project_01/code
Copyright 2019 Rebecca Liu

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
Software API:

  * opc.client ensures that server is running so that LED string can be displayed
  
--------------------------------------------------------------------------
Background Information: 
 
   * Base code for LED functions came from the following repositories:
        https://markayoder.github.io/PRUCookbook/01case/case.html#_neopixels_5050_rgb_leds_with_integrated_drivers_ledscape
        https://markayoder.github.io/PRUCookbook/06io/io.html#io_uio
        https://github.com/Yona-Appletree/LEDscape.git
        https://github.com/zestyping/openpixelcontrol

"""

import time
import opc
from button_template import Button


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
    
# Define Pixel String
STR_LEN=9
leds = []

# define ending colors for each LED 

colors = [
    
# original color RGB codes 
#     (255, 0, 0),      # Red
#     (255, 167, 0),    # Orange
#     (255, 153, 204),  # Pink
#     (255, 179, 153),  # Orange-Pink
#     (255, 204, 102),  # Yellow
#     (173, 162, 255),  # Purple
#     (7, 89, 165)      # Dark Blue

    # (51, 0, 0), # red
    # (51, 13, 0), # orange
    # (51,26,5), # yellow 
    # (51,22,25), # pink
    # (35,7,21), # purple
    # (51,22,25), # pink
    # (51,26,5), # yellow 
    # (51, 13, 0), # orange
    # (51, 0, 0), # red

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

# Create list of RGB colors for LEDs with initial colors 

for i in range(STR_LEN):
    leds.append(colors[i % len(colors)])
print(leds)

if not client.put_pixels(leds, channel=0):
    print ('not connected')

time.sleep(1)

# Uses each light's address to set display to set a color
def led_task():
    global leds # declare leds as global variable 
    transition_time = 30  # 5 minutes in seconds
    step = 1  # Step size to increase brightness
    start_time = time.time()
    led_button = Button("P2_2") # Yellow button for turning off LED lights 
    led_off = False
    
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
                    leds[i] = new_color


        if not client.put_pixels(leds, channel=0):
            print('not connected')
            
        
        time.sleep(0.1)

# End def            
        
if __name__ == '__main__':    
    try:
        led_task()
    except KeyboardInterrupt:
        pass

    print("Program Complete.")        
