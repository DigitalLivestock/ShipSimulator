class Rudder:
    def __init__(self):
        self.angle = 0.0 #0°-180°

    def set_rudder(self, value):
        if 0 <= value <= 180:
            self.angle = value
        else:
            print("invalid angle")

    def get_rudder(self):
        return self.angle
