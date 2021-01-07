from time           import sleep
from motors         import main_motor
from rudders        import main_rudder
from navigation.gps import gps

#Build boat:
motor   = main_motor()
rudder  = main_rudder()
gps     = gps()
vel     = velocity(motor, rudder, pos) #motor + rudder => pos

def main():
    motor.set_throttle(30)
    while True:
        sleep(1)
        gps.print_coordinates()

main()
