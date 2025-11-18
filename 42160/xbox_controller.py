# Control LEGO 42160 using XBOX controller.
# - Based on https://pybricks.com/project/technic-42160-xbox/
# - XBOX pairing instruction: https://docs.pybricks.com/en/latest/iodevices/xboxcontroller.html#xbox-controller-pairing-instructions

from pybricks.iodevices import XboxController
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import Car
from pybricks.tools import wait

# Set up all devices.
steering = Motor(Port.D, Direction.CLOCKWISE)
front = Motor(Port.B, Direction.CLOCKWISE)
rear = Motor(Port.A, Direction.CLOCKWISE)
car = Car(steering, [front, rear])
xbox = XboxController()


# The main program starts here.
while True:
    # Control steering using the left joystick.
    car.steer(xbox.joystick_left()[0])
    # Control drive power using the trigger buttons.
    car.drive_power(xbox.triggers()[1] - xbox.triggers()[0])
    wait(50)

