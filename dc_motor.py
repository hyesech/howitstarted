from gpiozero import Motor
from time import sleep

motor = Motor(forward=20, backward=21)


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

except KeyboardInterrupt:
    pass

