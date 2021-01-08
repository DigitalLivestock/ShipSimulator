import _thread as thread

class velocity:
    def __init__(self):
        self.speed = 0.0     #knots
        self.direction = 0.0 #0°-360°
        self.update_thread = 0
        #self.north = 0.0
        #self.south = 0.0
        #self.west  = 0.0
        #self.east  = 0.0

    def update_values(self, sync, motor, rudder):
        old_sync = 0
        while True:
            current_sync = sync.get_global_sync()
            if old_sync != current_sync:
                print("velocity.update_values: new sync")
                self.speed = motor.get_throttle()
                self.direction = rudder.get_rudder()
                old_sync = current_sync

    def start_velocity(self, sync, motor, rudder):
        self.update_thread = thread.start_new_thread(self.update_values, (sync, motor, rudder))
        print("start_velocity: started thread with update_values")

    #def set_speed(self, value):
    #    self.speed = motor.get_throttle()

    #def set_direction(self, value):
    #    self.direction = rudder.get_rudder()

    #ONLY TO BE USED BY position.py
    def get_speed(self):
        return self.speed

    def get_direction(self):
        return self.direction

    def get_velocity(self):
        return (self.speed, self.direction)
