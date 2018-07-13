#include "Streaming.h"
#include "SerialReceiver.h"
#include "set_pwm_frequency.h"

SerialReceiver receiver = SerialReceiver();

const int NumPwm = 6;
const int PwmPin[NumPwm] = {3,5,6,9,10,11};
const int PwmDiv[NumPwm] = {1,1,1,1,1,1};
const int PwmDefaultValue[NumPwm] = {0,0,0,0,0,0};
const int PwmMinValue = 0;
const int PwmMaxValue = 255;

bool check_pwm_pin(int pwm_pin);

void setup() 
{
    Serial.begin(9600);

    for (int i=0; i<NumPwm; i++) 
    {
        pinMode(PwmPin[i],OUTPUT);
        digitalWrite(PwmPin[i],LOW);
        setPwmFrequency(PwmPin[i],PwmDiv[i]);
        analogWrite(PwmPin[i],PwmDefaultValue[i]);
    }
}

void loop()
{
    while (Serial.available() > 0) {
        receiver.process(Serial.read());
        if (receiver.messageReady()) {
            if (receiver.numberOfItems() == 2)
            {
                int pwm_pin = receiver.readInt(0);
                int pwm_val = constrain(receiver.readInt(1),0,255);
                if (check_pwm_pin(pwm_pin))
                {
                    analogWrite(pwm_pin, pwm_val);
                    //Serial << "pwm_pin: " << pwm_pin << endl;
                    //Serial << "pwm_val: " << pwm_val << endl;
                }
            }
            receiver.reset();
        }
    }
    delay(10);
}

bool check_pwm_pin(int pwm_pin)
{
    bool ok = false;
    for (int i=0; i<NumPwm; i++)
    {
        if (PwmPin[i] == pwm_pin)
        {
            ok = true;
        }
    }
    return ok;
}



