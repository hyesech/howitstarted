from gpiozero import Motor
from time import sleep

# Definition of motor pin
FW = 22
BW = 27

# Set pin
motor = Motor(forward=FW, backward=BW)


# forward
def forward(delay):
    motor.forward()
    sleep(delay)


def back(delay):
    motor.backward()
    sleep(delay)


# run
try:
    while True:
        forward(1)
        back(1)

except KeyboardInterrupt:
    print("keyboard interrupt")
