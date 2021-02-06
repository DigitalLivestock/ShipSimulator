import _thread as thread
import math

#Don't use in user program! Use gps instead.
class Position:
    def __init__(self, x=0, y=0):
        self.x = 0.0
        self.y = 0.0

    def move_x(self, steps):
        self.x = steps

    def move_y(self, steps):
        self.y = steps

    def update_values(self, sync, vel):
        old_sync = 0
        while True:
            current_sync = sync.get_global_sync()
            if old_sync != current_sync:
                print("position.update_values: new sync")
                speed = vel.get_speed()*0.1
                deg = vel.get_direction()
                self.x += math.cos(math.radians(deg))*speed
                self.y += math.sin(math.radians(deg))*speed
                old_sync = current_sync

    def start_position(self, sync, vel):
        self.update_thread = thread.start_new_thread(self.update_values, (sync, vel))
        print("position.start_position: started thread with update_values")

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_pos(self):
        return (self.x, self.y)
