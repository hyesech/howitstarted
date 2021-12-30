from gpiozero import Servo
from time import sleep

servo = Servo(11)

try:
    while True:
        servo.min()
        sleep(2)
        servo.mid()
        sleep(2)
        servo.max()
        sleep(2)

except KeyboardInterrupt:
    print("keyboard interrupt")
