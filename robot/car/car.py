import time
import RPi.GPIO as GPIO

class Car():
    # 树莓派接L298N的enable A/B的引脚
    ENABLE_A = 33
    ENABLE_B = 32
    # IN1 ~ 4的引脚编号
    INS = [11, 12, 16, 18]
    def __init__(self):
        # 初始化引脚
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(Car.ENABLE_A, GPIO.OUT)
        GPIO.setup(Car.ENABLE_B, GPIO.OUT)
        for in_number in Car.INS:
            GPIO.setup(in_number, GPIO.OUT)

        self.pwm_left = GPIO.PWM(Car.ENABLE_A, 20)
        self.pwm_left.start(0)
        self.pwm_right = GPIO.PWM(Car.ENABLE_B, 20)
        self.pwm_right.start(0)

        self.motor_left = Car.INS[:2]
        self.motor_right = Car.INS[2:]

        self.state = {
            "base_speed": 0,
            "left_rate": 1,
            "right_rate": 1
        }

    def __del__(self):
        self.pwm_left.stop()
        self.pwm_right.stop()
        GPIO.cleanup()

    def __motor_forward(self, motor):
        GPIO.output(motor[0], GPIO.HIGH)
        GPIO.output(motor[1], GPIO.LOW)

    def __motor_backward(self, motor):
        GPIO.output(motor[1], GPIO.HIGH)
        GPIO.output(motor[0], GPIO.LOW)

    def __motor_stop(self, motor):
        GPIO.output(motor[0], GPIO.LOW)
        GPIO.output(motor[1], GPIO.LOW)

    def forward(self):
        self.__motor_forward(self.motor_left)
        self.__motor_forward(self.motor_right)

    def back(self):
        self.__motor_backward(self.motor_left)
        self.__motor_backward(self.motor_right)

    def stop(self):
        self.__motor_stop(self.motor_left)
        self.__motor_stop(self.motor_right)

    def left(self, rate):
        """
        左转弯的时候，右边轮胎速度不变，左边速度为右边速度 * rate
        rate值为0到1之间
        """
        self.state["left_rate"] = rate

    def right(self, rate):
        self.state["right_rate"] = rate

    def speed(self, val):
        self.state["base_speed"] = val
        self.pwm_left.ChangeDutyCycle(val * self.state["left_rate"])
        self.pwm_right.ChangeDutyCycle(val * self.state["right_rate"])

    def get_status(self):
        return self.state["base_speed"], \
            self.state["base_speed"] * self.state["left_rate"], \
            self.state["base_speed"] * self.state["right_rate"]