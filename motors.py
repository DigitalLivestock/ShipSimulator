class main_motor:
    def __init__(self):
        self.throttle = 0.0 #(-20)-30

    def set_throttle(self, value):
        if (-20) <= value <= 30:
            self.angle = value
        else:
            print("invalid throttle")
