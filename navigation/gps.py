import _thread as thread

#Mask class for position
class Gps:
    def __init__(self):
        self.x = 0
        self.y = 0

    def update_values(self, sync, pos):
        old_sync = 0
        while True:
            current_sync = sync.get_global_sync()
            if old_sync != current_sync:
                print("gps.update_values: new sync")
                self.x = pos.get_x()
                self.y = pos.get_y()
                old_sync = current_sync

    def start_gps(self, sync, pos):
        self.update_thread = thread.start_new_thread(self.update_values, (sync, pos))
        print("gps.start_velocity: started thread with update_values")

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_cords(self):
        return (self.x, self.y)

    def print_coordinates(self):
        print(str(self.x) + ":" + str(self.y))
