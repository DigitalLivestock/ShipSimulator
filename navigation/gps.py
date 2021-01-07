#Note: Can't be independent of mechanical parts
from physics.position import pos

class gps:
    def __init__(self):
        self.pos = pos()
        self.x = self.pos.get_x()
        self.y = self.pos.get_y()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def print_coordinates(self):
        print(str(self.x) + ":" + str(self.y))
