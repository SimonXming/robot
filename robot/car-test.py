from car.car import Car

if __name__ == '__main__':
    car = Car()
    car.forward()
    car.speed(20)
    time.sleep(5)
    car.speed(50)
    time.sleep(5)
    car.stop()
    time.sleep(5)
    car.back()
    car.speed(20)
    time.sleep(5)
    car.speed(50)
    time.sleep(5)
    del car
