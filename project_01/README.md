# Sunrise Alarm Clock

All the code to run this program should be in the folder `sunrise_alarm_clock`. The code should be downloaded and implemented in the PocketBeagle Cloud9 program. All the hardware and hardware implementation can be found in the hackster.io page: https://www.hackster.io/sp94/engi-301-sunrise-alarm-clock-e4a65d

## Steps to Run
1. Wire up all the components according to the Hackster diagram.
2. Connected the PocketBeagle to the internet.
3. Set up the PocketBeagle to run Python by running `sudo apt-get update`, `sudo apt-get install build-essential python-dev python setuptools python-smbus -y`, and `sudo apt-get install python-pip python3-pip -y`. 
Install Adafruit BBIO bu running `sudo pip3 install --upgrade Adafruit_BBIO`. 
4. Configure the GPIO pins that the buttons and LED strip lights are connected to. Run `configure_pins_buttons.sh` and `configure_pins_led.sh` in the terminal. 
5. Run `sudo ./run-opc-server` within the directory of sunrise_alarm_clock.
6. Run `main_alarm.py`.

## Explaining each python file 

The main files that are called within the system are `spi_screen.py`, `led_strip_test.py`, `button_template`, and `buzzer_template`. 

1. `spi_screen.py`: this file displays the current local time using Wifi on the SPI screen. It can be used to test whether this function works.
2. `led_strip_test.py`: this file can be used to test the LED lights. It slowly turns on LED lights and increases its brightness over 30 seconds. That time can be changed to any other time as well.
3. `button_template'`: this file holds the functions and tests whether a button works or not. The correct GPIO pin must be input into the code to test the correct button.
4. `buzzer_template`: this file can be used to test the buzzer. It is coded to play Viva la Vida's "Coldplay" and can be stopped by pressing the red button.

The other files are test files that I used to test previously written code for my hardware. There is also a folder called LED that contains all the original LED strip lights files. 

