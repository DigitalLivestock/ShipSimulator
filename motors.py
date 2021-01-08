class main_motor:
    def __init__(self):
        self.throttle = 0.0 #(-20)-30

    def set_throttle(self, value):
        if (0.0 <= value) and (value <= 30.0):
            self.throttle = value
        else:
            print("invalid throttle")

    def get_throttle(self):
        return self.throttle

if "__main__" == __name__:
    print("--Test: motor--")
    motor = main_motor()
    print("Current throttle: " + str(motor.get_throttle()))
    print("[*]Testing set_throttle():")
    motor.set_throttle(15.0)
    print("New throttle is: " + str(motor.get_throttle()))
    print("--Test Done!--")
