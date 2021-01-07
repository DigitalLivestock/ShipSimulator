from position import pos

class velocity:
    def init(self):
        self.speed = 0.0     #knots
        self.direction = 0.0 #0°-360°
        #self.north = 0.0
        #self.south = 0.0
        #self.west  = 0.0
        #self.east  = 0.0

    def set_speed(self, value):
        self.speed = value

    def set_direction(self, value):
        self.direction = value

    def get_speed(self):
        return self.speed

    def get_direction(self):
        return self.direction
