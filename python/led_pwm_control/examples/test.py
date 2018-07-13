from __future__ import print_function
import time
from led_pwm_control import LEDController 
import numpy

pin = 3
dt = 0.01
cycles = 5
period = 5.0
max_value = 255

num_pts = int((cycles*period)/dt)
t_vals = numpy.linspace(0.0,period*cycles,num_pts)
pwm_vals = max_value*0.5*(1.0 - numpy.cos(2.0*numpy.pi*t_vals/period))

dev = LEDController('/dev/ttyUSB0')

for i, pwm in enumerate(pwm_vals):
    dev.set_value(pin, pwm)
    print('{}/{}: {}'.format(i,pwm_vals.shape[0],pwm))
    time.sleep(t_vals[1]-t_vals[0])


