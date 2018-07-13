from __future__ import print_function
import time
import serial

class LEDController(serial.Serial):

    ResetSleepDt = 2.0
    Baudrate = 9600 
    MaxPwmValue = 255
    MinPwmValue = 0
    AllowedPins = [3,5,6,9,10,11]

    def __init__(self,port,timeout=10.0):
        param = {'baudrate': self.Baudrate, 'timeout': timeout}
        super(LEDController,self).__init__(port,**param)
        time.sleep(self.ResetSleepDt)

    def set_value(self,pin_num, pwm_val):
        if not pin_num in self.AllowedPins:
            raise ValueError, 'pwm value not allowd'
        if pwm_val < self.MinPwmValue or pwm_val > self.MaxPwmValue:
            raise ValueError, 'pwm value out of range'
        cmd = '[{}, {}]'.format(pin_num,pwm_val)
        self.write('{}\n'.format(cmd))

# -------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    import sys
    port = sys.argv[1]
    dev = LEDController(port)

    done = False
    while not done:
        input_str = raw_input('enter pin, pwm (q=quit): ')
        if input_str == 'q':
            exit(0)
        else:
            input_list = input_str.split(' ')
            input_list = [int(x) for x in input_list]
            pin_num = input_list[0]
            pwm_val = input_list[1]
            dev.set_value(pin_num, pwm_val)










