from time                import sleep
from motors              import Motor
from rudders             import Rudder
from chart               import Chart
from navigation.manual   import Manual
from navigation.gps      import Gps
from sensors.speedometer import *
from sensors.compass     import *
from physics.position    import Position
from physics.velocity    import Velocity
from sync                import *

#Sync:
env_sync = Sync()
sync_handle = Sync_handler(env_sync, 2)

#Build boat:
motor = Motor()
rudder = Rudder()

#Physics:
vel = Velocity() #motor + rudder => pos
pos = Position()

#Navigation:
gps_cords = Gps()
chart = Chart()
manual = Manual()

#Sensors:
#spm = Speedometer()
#cps = Compass()

#Start threads: They all update at once. Could cause latency in updates as updates are skipped.
vel.start_velocity(env_sync, motor, rudder) #motor and rudder must be directly passed
pos.start_position(env_sync, vel)
gps_cords.start_gps(env_sync, pos)
chart.start_chart(env_sync, gps_cords)
manual.start_panel()
#spm.start_speedometer(env_sync, vel)
#cps.start_compass(env_sync, vel)

#database_x = []
#database_y = []

def main():

    while True:
        #database_x.append(gps_cords.get_x())
        #database_y.append(gps_cords.get_y())
        motor.set_throttle(manual.get_throttle())
        rudder.set_rudder(manual.get_rudder())

        sleep(0.5)
        print("-Motor: throttle is now: " + str(motor.get_throttle()))
        print("-Velocity: Speed is now: " + str(vel.get_speed()))
        print("-Position: Position is now: " + str(pos.get_pos()))
        print("-GPS: Cords are now: " + str(gps_cords.get_cords()))

main()
