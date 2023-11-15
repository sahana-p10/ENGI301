# Sunrise Alarm Clock

All the code to run this program should be in the folder `sunrise_alarm_clock`. The code should be downloaded and implemented in the PocketBeagle Cloud9 program. 

## Steps to Run 
1. Configure the GPIO pins that the buttons and LED strip lights are connected to. Run `configure_pins_buttons.sh` and `configure_pins_led.sh`.
2. Run `sudo ./run-opc-server` within the directory of sunrise_alarm_clock.
3. Run `main_alarm.py`.

## Explaining each python file 

The main files that are called within the system are `spi_screen.py`, `led_strip_test.py`, `button_template`, and `buzzer_template`. 

1. `spi_screen.py`: this file displays the current local time using Wifi on the SPI screen. It can be used to test whether this function works.
2. `led_strip_test.py`: this file can be used to test the LED lights. It slowly turns on LED lights and increases its brightness over 30 seconds. That time can be changed to any other time as well.
3. `button_template'`: this file holds the functions and tests whether a button works or not. The correct GPIO pin must be input into the code to test the correct button.
4. `buzzer_template`: this file can be used to test the buzzer. It is coded to play Viva la Vida's "Coldplay" and can be stopped by pressing the red button.
