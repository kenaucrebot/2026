# =============================================================================
#  FIRST LEGO League — Mission Run Selector
#  Author: Coach Mark Smith-Guerrero
# =============================================================================
#  FIRST LEGO League — Mission Run Selector
#  Author: Coach Mark Smith-Guerrero, Kendall Painley, Ken Aucremanne
#
#  HOW TO START A RUN
#    1. Start this program (center button on the hub).
#    2. Hold a colored LEGO piece in front of the color sensor (Port E).
#       The hub light changes to the color it sees, and the display shows
#       the run number (1, 2, 3 or 4).
#    3. Press LEFT or RIGHT to start that run.
#    4. When the run ends, the robot beeps and waits for the next selection.
#
#  HOW TO CUSTOMIZE
#    - Change robot measurements and default speeds in SECTION 1.
#    - Write your missions inside the run functions in SECTION 4 and 5.
#    - Add, remove, or recolor runs in the RUN TABLE in SECTION 6.
#    - See README.md for the full library reference and hints.
# =============================================================================

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Direction, Port, Stop, Icon, Color
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


# =============================================================================
#  SECTION 1: SETTINGS  (change these numbers to tune the robot)
# =============================================================================

WHEEL_DIAMETER = 43         # mm — re-measure if you change wheels
AXLE_TRACK = 114            # mm — distance between where the wheels touch the mat

# Standard drive settings. These are restored before every run.
DEFAULT_STRAIGHT_SPEED = 150    # mm/s
DEFAULT_STRAIGHT_ACCEL = 563    # mm/s²
DEFAULT_TURN_RATE = 125         # deg/s
DEFAULT_TURN_ACCEL = 565        # deg/s²

# Color sensor
PRESENT_THRESHOLD = 15      # reflection above this means a LEGO piece is in front
LOOP_DELAY = 50             # ms between sensor checks

# Set to True while testing to print sensor readings to the terminal.
DEBUG = False


# =============================================================================
#  SECTION 2: HARDWARE SETUP  (matches the Hardware Map in README.md)
# =============================================================================

hub = PrimeHub()

sensor = ColorSensor(Port.E)
# Only report colors we use. This reduces wrong readings.
sensor.detectable_colors([Color.RED, Color.WHITE, Color.BLUE, Color.NONE])

left_drive = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_drive = Motor(Port.B, Direction.CLOCKWISE)
drive_base = DriveBase(left_drive, right_drive, WHEEL_DIAMETER, AXLE_TRACK)
drive_base.use_gyro(True)

left_attachment = Motor(Port.C, Direction.CLOCKWISE)
right_attachment = Motor(Port.D, Direction.CLOCKWISE)


# =============================================================================
#  SECTION 3: HELPER FUNCTIONS  (reusable moves for any run)
# =============================================================================

def reset_drive_settings():
    """Put speeds back to the team defaults."""
    drive_base.settings(
        straight_speed=DEFAULT_STRAIGHT_SPEED,
        straight_acceleration=DEFAULT_STRAIGHT_ACCEL,
        turn_rate=DEFAULT_TURN_RATE,
        turn_acceleration=DEFAULT_TURN_ACCEL,
    )


def set_speed(straight=None, turn=None):
    """Change speed partway through a run. Example: set_speed(straight=400)"""
    if straight is not None:
        drive_base.settings(straight_speed=straight)
    if turn is not None:
        drive_base.settings(turn_rate=turn)


def stop_all():
    """Stop the drive base and both attachment motors."""
    drive_base.stop()
    left_attachment.stop()
    right_attachment.stop()


def wait_for_release():
    """Wait until no buttons are held, so one press doesn't start two runs."""
    while hub.buttons.pressed():
        wait(10)


def square_up(speed=-100, time=800):
    """Back into a wall for a moment to straighten the robot.
    Use a negative speed to back up, positive to drive forward into a wall."""
    drive_base.drive(speed, 0)
    wait(time)
    drive_base.stop()
    drive_base.reset()
    hub.imu.reset_heading(0)


def zero_attachment(motor, speed=-200, duty_limit=40):
    """Push an attachment gently against its stop and call that angle 0.
    After this, run_target() positions are repeatable."""
    motor.run_until_stalled(speed, then=Stop.HOLD, duty_limit=duty_limit)
    motor.reset_angle(0)


def drive_until_color(target_color, speed=100, timeout=5000):
    """Drive forward until the color sensor sees target_color.
    Only useful if the sensor can also point at the mat.
    Stops after `timeout` ms as a safety. Returns True if the color was found."""
    timer = StopWatch()
    drive_base.drive(speed, 0)
    found = False
    while timer.time() < timeout:
        if sensor.color() == target_color:
            found = True
            break
        wait(10)
    drive_base.stop()
    return found


def finished_signal():
    """Beep and show a happy face when a run finishes."""
    hub.speaker.beep(800, 100)
    hub.display.icon(Icon.HAPPY)


# =============================================================================
#  SECTION 4: LEFT RUNS  (press the LEFT button)
#
#  Fill in the header comment for each run, then replace the example
#  steps with your mission. Test one line at a time.
# =============================================================================

def left_run1():
    # Mission:        ____________________
    # Start position: ____________________
    # Attachment:     ____________________
    # Points:         ___
    # Success rate:   __/10 (tested ____-__-__)

    # Example steps — replace with your mission:
    # zero_attachment(left_attachment)            # 1. zero the arm
    # drive_base.straight(300)                    # 2. drive out 300 mm
    # drive_base.turn(90)                         # 3. turn right 90 degrees
    # left_attachment.run_target(300, 90)         # 4. move arm to 90 degrees
    # drive_base.straight(-300)                   # 5. back up toward home
    hub.speaker.beep()


def left_run2():
    # Mission:        ____________________
    # Start position: ____________________
    # Attachment:     ____________________
    # Points:         ___
    # Success rate:   __/10 (tested ____-__-__)

    # Example: run an attachment WHILE driving using wait=False
    right_attachment.run_angle(300, 180, wait=False)
    drive_base.straight(250)
    hub.speaker.beep()


def left_run3():
    # Mission:        ____________________
    # Start position: ____________________
    # Attachment:     ____________________
    # Points:         ___
    # Success rate:   __/10 (tested ____-__-__)

    # Example: slow for precision, fast for the trip home
    set_speed(straight=100)
    drive_base.straight(200)
    set_speed(straight=400)
    drive_base.straight(-200)
    hub.speaker.beep()


def left_run4():
    # Mission:        ____________________
    # Start position: ____________________
    # Attachment:     ____________________
    # Points:         ___
    # Success rate:   __/10 (tested ____-__-__)

    # Example: slow for precision, fast for the trip home
    set_speed(straight=100)
    drive_base.straight(200)
    set_speed(straight=400)
    drive_base.straight(-200)
    hub.speaker.beep()

# =============================================================================
#  SECTION 5: RIGHT RUNS  (press the RIGHT button)
# =============================================================================

def right_run1():
    # Mission:        ____________________
    # Start position: ____________________
    # Attachment:     ____________________
    # Points:         ___
    # Success rate:   __/10 (tested ____-__-__)
    zero_attachment(left_attachment)            # 1. zero the arm
    drive_base.straight(300)                    # 2. drive out 300 mm
    drive_base.turn(90)                         # 3. turn right 90 degrees
    left_attachment.run_target(300, 90)         # 4. move arm to 90 degrees
    drive_base.straight(-300)                   # 5. back up toward home
    hub.speaker.beep()


def right_run2():
    # Mission:        ____________________
    # Start position: ____________________
    # Attachment:     ____________________
    # Points:         ___
    # Success rate:   __/10 (tested ____-__-__)
    zero_attachment(left_attachment)            # 1. zero the arm
    drive_base.straight(300)                    # 2. drive out 300 mm
    drive_base.turn(90)                         # 3. turn right 90 degrees
    left_attachment.run_target(300, 90)         # 4. move arm to 90 degrees
    drive_base.straight(-300)                   # 5. back up toward home
    hub.speaker.beep()


def right_run3():
    # Mission:        ____________________
    # Start position: ____________________
    # Attachment:     ____________________
    # Points:         ___
    # Success rate:   __/10 (tested ____-__-__)
    zero_attachment(left_attachment)            # 1. zero the arm
    drive_base.straight(300)                    # 2. drive out 300 mm
    drive_base.turn(90)                         # 3. turn right 90 degrees
    left_attachment.run_target(300, 90)         # 4. move arm to 90 degrees
    drive_base.straight(-300)                   # 5. back up toward home
    hub.speaker.beep()


def right_run4():
    # Mission:        ____________________
    # Start position: ____________________
    # Attachment:     ____________________
    # Points:         ___
    # Success rate:   __/10 (tested ____-__-__)
    zero_attachment(left_attachment)            # 1. zero the arm
    drive_base.straight(300)                    # 2. drive out 300 mm
    drive_base.turn(90)                         # 3. turn right 90 degrees
    left_attachment.run_target(300, 90)         # 4. move arm to 90 degrees
    drive_base.straight(-300)                   # 5. back up toward home
    hub.speaker.beep()

# =============================================================================
#  SECTION 6: RUN TABLE  (which color + button starts which run)
#
#  Each row is: (color, run number shown on display, left run, right run)
#  To add a run:
#    1. Write a new function above (for example, left_run4).
#    2. Add the color to sensor.detectable_colors() in SECTION 2.
#    3. Add a row below.
#  Use None if a color has no run for one side.
# =============================================================================

RUN_TABLE = [
    # color        number  LEFT button   RIGHT button
    (Color.RED,    1,      left_run1,    right_run1),
    (Color.WHITE,  2,      left_run2,    right_run2),
    (Color.BLUE,   3,      left_run3,    right_run3),
    (Color,GREEN,  4,      left_run4,    right_run4),
]


def find_row(color):
    """Return the RUN_TABLE row for this color, or None if there isn't one."""
    for row in RUN_TABLE:
        if row[0] == color:
            return row
    return None


# =============================================================================
#  SECTION 7: RUN LAUNCHER  (you usually don't need to change this)
# =============================================================================

def start_run(run):
    """Prepare the robot, do the run, then clean up."""
    wait_for_release()
    hub.light.on(Color.GREEN)       # green = running
    hub.display.off()

    reset_drive_settings()
    drive_base.reset()              # distance and angle back to 0
    hub.imu.reset_heading(0)        # current direction = 0 degrees

    run()

    stop_all()
    reset_drive_settings()
    finished_signal()


def main():
    hub.speaker.beep(600, 100)      # ready signal
    hub.display.icon(Icon.HAPPY)

    while True:
        pressed = hub.buttons.pressed()
        color = sensor.color()
        reflection = sensor.reflection()

        if DEBUG:
            print(color, reflection)

        row = find_row(color)

        if reflection > PRESENT_THRESHOLD and row is not None:
            # A known color is in front of the sensor: show it.
            hub.light.on(color)
            hub.display.number(row[1])

            if Button.LEFT in pressed and row[2] is not None:
                start_run(row[2])
            elif Button.RIGHT in pressed and row[3] is not None:
                start_run(row[3])
        else:
            hub.light.off()

        wait(LOOP_DELAY)


main()

