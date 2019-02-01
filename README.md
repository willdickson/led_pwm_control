## led_pwm_control 

Software and firmware for controlling LEDs via PWM using and arduino.

## Installation

Requirements:  python-serial, python-numpy (for example only)

```bash
$ python setup.py install 

```

#### Python library example 

```python
from led_pwm_control import LEDController 
dev = LEDController('/dev/ttyUSB0')
dev.set_value(3,100)  # set value of pwm on pin 3 to 100

```

