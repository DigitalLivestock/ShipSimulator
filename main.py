from time                import sleep
from motors              import main_motor
from rudders             import main_rudder
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

#Sensors:
#spm = speedometer.speedometer()
#cps = compass.compass()

#Start threads: They all update at once. Could cause latency in updates as updates are skipped.
vel.start_velocity(env_sync, motor, rudder) #motor and rudder must be directly passed
pos.start_position(env_sync, vel)
gps_cords.start_gps(env_sync, pos)
#spm.start_speedometer(env_sync, vel)
#cps.start_compass(env_sync, vel)

def main():
    motor.set_throttle(30)
    rudder.set_rudder(135)

    for i in range(10):
        sleep(1)
        print("-Motor: throttle is now: " + str(motor.get_throttle()))
        print("-Velocity: Speed is now: " + str(vel.get_speed()))
        print("-Position: Position is now: " + str(pos.get_pos()))
        print("-GPS: Cords are now: " + str(gps_cords.get_cords()))

main()
