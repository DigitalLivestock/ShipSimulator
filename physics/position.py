class pos:
    def __init__(self, x=0, y=0):
        self.x = 0.0
        self.y = 0.0

    def move_x(self, steps):
        self.x = steps

    def move_y(self, steps):
        self.y = steps

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
