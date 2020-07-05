
import time
from camera.library.PCA9685 import PCA9685

if __name__=='__main__':
    pwm = PCA9685(0x40, debug=False)
    pwm.setPWMFreq(50)
    while True:
        # setServoPulse(2,2500)
        for i in range(500,2500,10):
            pwm.setServoPulse(0,i)
            time.sleep(0.02)

        for i in range(2500,500,-10):
            pwm.setServoPulse(0,i)
            time.sleep(0.02)

        for i in range(1500,2500,10):
            pwm.setServoPulse(1,i)
            time.sleep(0.02)

        for i in range(2500,1500,-10):
            pwm.setServoPulse(1,i)
            time.sleep(0.02)
