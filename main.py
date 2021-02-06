from time                import sleep
from motors              import main_motor
from rudders             import main_rudder
from chart               import Chart
from navigation.manual   import Manual
import navigation.gps       as gps
import sensors.speedometer  as speedometer
import sensors.compass      as compass
import physics.position     as position
import physics.velocity     as velocity
import sync

#Backend:
env_sync = sync.sync()
sync_handle = sync.sync_handler(env_sync, 2)

#Build boat:
motor = main_motor()
rudder = main_rudder()

#Physics:
vel = velocity.velocity() #motor + rudder => pos
pos = position.position()

#Navigation:
gps_cords = gps.gps()
chart = Chart()
manual = Manual()

#Sensors:
#spm = speedometer.speedometer()
#cps = compass.compass()

#Start threads: They all update at once. Could cause latency in updates as updates are skipped.
vel.start_velocity(env_sync, motor, rudder) #motor and rudder must be directly passed
pos.start_position(env_sync, vel)
gps_cords.start_gps(env_sync, pos)
chart.start_chart(env_sync, gps_cords)
manual.start_panel()
#chart.start_update_path(env_sync, gps_cords)
#spm.start_speedometer(env_sync, vel)
#cps.start_compass(env_sync, vel)

database_x = []
database_y = []

def main():

    for i in range(30):
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
