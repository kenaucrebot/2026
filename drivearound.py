# Author: Coach Mark Smith-Guerrero

from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

# Set up.
hub = PrimeHub()
left_drive = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_drive = Motor(Port.B, Direction.CLOCKWISE)

Robot = DriveBase(left_drive, right_drive, 43, 114)
Robot.use_gyro(True)

left_attachment = Motor(Port.C, Direction.CLOCKWISE)
right_attachment = Motor(Port.D, Direction.CLOCKWISE)

heading_error = 0

def forward(mm, speed=300):
    Robot.straight(mm)

def right(angle):
    Robot.turn(angle)

def left(angle):
    Robot.turn(-angle)

#forward(50)
#left(90)
#right(90)


    



