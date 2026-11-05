FIRST LEGO League Robot Code (Pybricks Python)

This repository holds our team's robot code for FIRST LEGO League (FLL). We write text-based Python with Pybricks instead of the LEGO block (Scratch-style) editor.

The robot is built on a LEGO SPIKE Prime / MINDSTORMS Robot Inventor hub. One program, main.py, holds every mission run. To choose a run:

Place a colored LEGO piece in front of the color sensor.
Press the LEFT or RIGHT button on the hub.

The color picks which run. The button picks the left or right set of runs. For example, you can use LEFT runs for missions launched from the left home area and RIGHT runs for the right home area.

Table of Contents
Robot Hardware Map
Getting Started
How the Program Works
Pybricks Libraries Reference
Units Cheat Sheet
Corrected Starter Template
Writing a Mission Run, Step by Step
Helpful Hints
Common Mistakes
Documenting Your Work
Resources
1. Robot Hardware Map
Port	Device	Variable name	Notes
A	Motor	left_drive	Left wheel, set to Direction.COUNTERCLOCKWISE so "forward" is positive
B	Motor	right_drive	Right wheel, Direction.CLOCKWISE
C	Motor	left_attachment	Left tool motor
D	Motor	right_attachment	Right tool motor
E	Color Sensor	sensor	Reads the colored LEGO piece that selects a run

Drive base measurements (used by DriveBase):

Wheel diameter: 43 mm
Axle track (distance between the centers of the two wheels where they touch the ground): 114 mm

If you change wheels or move them, re-measure these numbers. Wrong values make every distance and turn inaccurate.

Run selection map (fill this in as your team creates runs):

Color	LEFT button	RIGHT button
Red	left_run1() — mission name here	right_run1() — mission name here
White	left_run2() — mission name here	right_run2() — mission name here
Blue	left_run3() — mission name here	right_run3() — mission name here
2. Getting Started
Step 1: Install Pybricks firmware on the hub
Open code.pybricks.com in Google Chrome or Microsoft Edge. These browsers support the Bluetooth and USB features it needs.
Click the gear (Settings) icon, then Install Pybricks Firmware.
Follow the on-screen steps. You can reinstall the official LEGO firmware later if you need it.
Step 2: Get the code
Download or clone this repository.
In Pybricks Code, use Import a file to open main.py.
Step 3: Connect and run
Turn on the hub.
Click the Bluetooth button in Pybricks Code and pick your hub.
Click Run (▶). The program downloads to the hub and starts.
Output from print() appears in the terminal at the bottom of the screen.

Tip: Once downloaded, the program stays on the hub. At competition you can start it with the hub's center button, with no laptop needed. Pressing the center button again stops it.

3. How the Program Works

The program runs a loop that repeats every 50 milliseconds:

Reset drive settings to the team's standard speeds. A run might change them, and this undoes those changes.
Read the buttons to see if LEFT or RIGHT is pressed.
Read the color sensor: both the color() and the reflection() value.
Check if a LEGO piece is present. If reflection is above 15, something is close to the sensor. The hub light changes to match the color it sees. This lets you confirm the reading before you press a button.
Start a run if a button is pressed. The color and button together choose the run.
Turn the light off if nothing is in front of the sensor.
Wait 50 ms and repeat.

When a run function finishes, the program returns to the loop so you can pick the next run.

4. Pybricks Libraries Reference

Each import line pulls in a set of tools. Here is what each one does, with the most useful features.

pybricks.hubs → PrimeHub

Controls the hub itself: lights, screen, buttons, speaker, and built-in gyro.

python
hub = PrimeHub()
Feature	Example	What it does
Status light	hub.light.on(Color.GREEN) / hub.light.off()	Changes the center button light
Blink light	hub.light.blink(Color.RED, [200, 200])	Blinks on 200 ms, off 200 ms
Display icon	hub.display.icon(Icon.HAPPY)	Shows a picture on the 5×5 grid
Display text	hub.display.text("GO")	Scrolls text
Display number	hub.display.number(42)	Shows a number
Buttons	hub.buttons.pressed()	Returns the set of buttons held right now
Beep	hub.speaker.beep(500, 100)	500 Hz tone for 100 ms
Heading	hub.imu.heading()	Which way the robot points, in degrees
Reset heading	hub.imu.reset_heading(0)	Sets the current direction as 0°
Tilt	hub.imu.tilt()	Returns (pitch, roll)
Battery	hub.battery.voltage()	Battery voltage in millivolts
pybricks.pupdevices → Motor, ColorSensor

"PUP" stands for Powered Up, the LEGO connector family used by SPIKE Prime.

Motor
python
left_attachment = Motor(Port.C, Direction.CLOCKWISE)
Method	Example	What it does
run_angle	left_attachment.run_angle(300, 90)	Turn 90° at 300 deg/s, then stop
run_target	left_attachment.run_target(300, 0)	Go to an exact angle (great for "arm down" / "arm up" positions)
run_time	left_attachment.run_time(500, 1000)	Spin at 500 deg/s for 1 second
run_until_stalled	left_attachment.run_until_stalled(-200, duty_limit=50)	Spin until it hits something. Useful for finding a starting position
run	left_attachment.run(400)	Spin forever until told to stop
stop / brake / hold	left_attachment.hold()	Stop and coast, brake, or actively hold position
angle	left_attachment.angle()	Current angle in degrees
reset_angle	left_attachment.reset_angle(0)	Call the current position 0°
speed	left_attachment.speed()	Current speed in deg/s
done	left_attachment.done()	True when a motion has finished
stalled	left_attachment.stalled()	True if the motor is stuck

The wait= option: Most motion commands accept wait=False. This starts the motion and moves on to the next line immediately. Use it to run an attachment while the robot drives:

python
left_attachment.run_angle(300, 180, wait=False)  # arm starts moving...
drive_base.straight(200)                          # ...while the robot drives

The then= option: Controls what the motor does when it finishes. Choices are Stop.HOLD (default, holds position), Stop.BRAKE, Stop.COAST, or Stop.NONE.

ColorSensor
python
sensor = ColorSensor(Port.E)
Method	Example	What it does
color()	sensor.color()	Returns a color like Color.RED, or Color.NONE
reflection()	sensor.reflection()	Reflected light, 0 (dark) to 100 (bright)
ambient()	sensor.ambient()	Light in the room, 0 to 100
hsv()	sensor.hsv()	Exact hue, saturation, value reading
detectable_colors()	sensor.detectable_colors([Color.RED, Color.WHITE, Color.BLUE, Color.NONE])	Limits which colors the sensor can report. Reduces wrong guesses
pybricks.parameters

Named constants so code is readable instead of full of mystery numbers.

Name	Common values	Used for
Port	Port.A … Port.F	Which hub port a device is plugged into
Direction	CLOCKWISE, COUNTERCLOCKWISE	Which way counts as "positive" for a motor
Stop	HOLD, BRAKE, COAST, NONE	What a motor does after a move
Color	RED, WHITE, BLUE, GREEN, YELLOW, BLACK, NONE …	Sensor readings and hub light colors
Button	LEFT, RIGHT, CENTER, BLUETOOTH	Hub buttons
Icon	HAPPY, SAD, UP, DOWN, HEART …	Pictures for the display
Side	TOP, FRONT, LEFT …	Which way the hub is mounted (for display rotation or gyro setup)

Color names are ALL CAPS. Write Color.RED, not Color.Red.

pybricks.robotics → DriveBase

Treats the two drive motors as one robot so you can say "drive 300 mm" instead of "spin each wheel 2.2 turns."

python
drive_base = DriveBase(left_drive, right_drive, 43, 114)
drive_base.use_gyro(True)
Method	Example	What it does
straight	drive_base.straight(300)	Drive forward 300 mm (negative = backward)
turn	drive_base.turn(90)	Spin in place 90° (positive = right/clockwise)
curve	drive_base.curve(200, 90)	Drive along a curve of radius 200 mm for 90°
drive	drive_base.drive(150, 0)	Drive at 150 mm/s forever, until stop()
stop / brake	drive_base.stop()	Stop the robot
distance	drive_base.distance()	Millimeters driven since last reset
angle	drive_base.angle()	Degrees turned since last reset
reset	drive_base.reset()	Zero the distance and angle
settings	drive_base.settings(straight_speed=300)	Change speed and acceleration
use_gyro	drive_base.use_gyro(True)	Use the hub's gyro to drive straighter and turn more accurately

settings() parameters:

Parameter	Unit	Our default	Raise it to...	Lower it to...
straight_speed	mm/s	150	go faster	be more precise
straight_acceleration	mm/s²	563	start/stop quicker	avoid wheel slip
turn_rate	deg/s	125	turn faster	turn more precisely
turn_acceleration	deg/s²	565	snap into turns	avoid skidding
pybricks.tools → wait
Tool	Example	What it does
wait	wait(500)	Pause for 500 milliseconds
StopWatch	timer = StopWatch(); timer.time()	Measure elapsed time in ms. Useful for timeouts
pybricks.iodevices → XboxController

Lets a Bluetooth Xbox controller drive the robot. It is imported in the example but not used in competition code, since remote control isn't allowed during FLL matches. It can be handy for practice or for finding positions on the mat. Remove the import if you don't need it.

5. Units Cheat Sheet
Quantity	Unit
Distance	millimeters (mm) — 10 mm = 1 cm
Drive speed	mm per second
Motor angle	degrees — 360 = one full turn
Motor speed	degrees per second
Turning	degrees — positive = clockwise (right)
Time	milliseconds — 1000 ms = 1 second
6. Corrected Starter Template

The original example has a few bugs that keep it from running (see Common Mistakes). This version fixes them and adds some helpful extras.

python
# Author: Coach Mark Smith-Guerrero

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Direction, Port, Stop, Icon, Color
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# ---------- Set up ----------
hub = PrimeHub()
sensor = ColorSensor(Port.E)
left_drive = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_drive = Motor(Port.B, Direction.CLOCKWISE)
drive_base = DriveBase(left_drive, right_drive, 43, 114)
drive_base.use_gyro(True)
left_attachment = Motor(Port.C, Direction.CLOCKWISE)
right_attachment = Motor(Port.D, Direction.CLOCKWISE)

# Only report the colors we actually use. This cuts down on wrong readings.
sensor.detectable_colors([Color.RED, Color.WHITE, Color.BLUE, Color.NONE])


# ---------- Helper ----------
def wait_for_release():
    """Wait until no buttons are pressed so one press doesn't start two runs."""
    while hub.buttons.pressed():
        wait(10)


# ---------- LEFT runs ----------
def left_run1():
    # Mission: ____________   Start position: ____________
    hub.speaker.beep()


def left_run2():
    # Mission: ____________   Start position: ____________
    hub.speaker.beep()


def left_run3():
    # Mission: ____________   Start position: ____________
    hub.speaker.beep()


# ---------- RIGHT runs ----------
def right_run1():
    # Mission: ____________   Start position: ____________
    hub.speaker.beep()


def right_run2():
    # Mission: ____________   Start position: ____________
    hub.speaker.beep()


def right_run3():
    # Mission: ____________   Start position: ____________
    hub.speaker.beep()


# ---------- Run selector ----------
LEFT_RUNS = {Color.RED: left_run1, Color.WHITE: left_run2, Color.BLUE: left_run3}
RIGHT_RUNS = {Color.RED: right_run1, Color.WHITE: right_run2, Color.BLUE: right_run3}


def start_run(run):
    wait_for_release()
    drive_base.reset()            # zero distance and angle
    hub.imu.reset_heading(0)      # current direction = 0 degrees
    run()
    drive_base.stop()             # make sure the robot is stopped afterward
    left_attachment.stop()
    right_attachment.stop()


def main():
    while True:
        # Reset standard drive settings in case a run changed them
        drive_base.settings(straight_speed=150, straight_acceleration=563,
                            turn_rate=125, turn_acceleration=565)
        pressed = hub.buttons.pressed()
        color = sensor.color()
        reflection = sensor.reflection()

        if reflection > 15:
            hub.light.on(color)
            if Button.LEFT in pressed and color in LEFT_RUNS:
                start_run(LEFT_RUNS[color])
            elif Button.RIGHT in pressed and color in RIGHT_RUNS:
                start_run(RIGHT_RUNS[color])
        else:
            hub.light.off()
        wait(50)


main()

What changed and why:

Every function now starts with def and has the correct name, such as left_run1.
Functions are defined above main() is called, so Python knows about them.
Color.Red was changed to Color.RED.
Dictionaries map each color to a run. This removes the if/elif chain where it's easy to make mistakes.
wait_for_release() stops a single button press from triggering a run twice.
start_run() resets the gyro and distance before each run and stops all motors afterward.
The print() in the loop was removed because it floods the terminal. Add it back while testing the color sensor.
Unused imports (XboxController, Side) and the unused heading_error variable were removed.
7. Writing a Mission Run, Step by Step
Pick the mission from the FLL game rules and write its name in the comment at the top of the run function.
Choose a start position in the home area. Use a jig (a LEGO guide piece) or a mark on the mat so the robot starts in the exact same spot every time. Write the position in the comment.
Plan the path on paper. Break it into small moves: "forward 400 mm, turn right 90°, forward 250 mm, lower arm."
Code one move at a time. Test after each new line.
Measure and adjust. If the robot stops 20 mm short, add 20 to the distance.
Add the return trip so the robot ends in the home area.
Test it 10 times in a row. If it works fewer than 8 out of 10 times, slow it down or add alignment (see hints below).
Update the run selection table in Section 1 and commit your changes.

Example run:

python
def left_run1():
    # Mission: Lift the flag   Start position: left home, against the back wall
    drive_base.straight(400)                    # drive out to the model
    drive_base.turn(90)                         # face the flag
    left_attachment.run_angle(300, -90)         # lower the arm
    drive_base.straight(50)                     # push in
    left_attachment.run_angle(300, 90)          # lift the flag
    drive_base.straight(-50)                    # back away
    drive_base.turn(-90)
    drive_base.settings(straight_speed=400)     # hurry home
    drive_base.straight(-400)
8. Helpful Hints
Accuracy
Slower is more accurate. Get a run working at low speed first, then speed up the parts that don't need precision (like driving home).
Square up against walls. Drive backward into the edge of the board for a moment to straighten the robot:
python
  drive_base.drive(-100, 0)
  wait(800)
  drive_base.stop()
Check the battery. Runs behave differently on a low battery. Charge before practice and competition. print(hub.battery.voltage()) shows the level; over about 7,800 mV is good.
Keep wheels and the mat clean. Dust makes wheels slip.
Attachments
Zero the arm at the start of a run. Push it against a stop, then reset the angle. After that, run_target positions are repeatable:
python
  left_attachment.run_until_stalled(-200, then=Stop.HOLD, duty_limit=40)
  left_attachment.reset_angle(0)
  left_attachment.run_target(300, 90)   # now 90 always means the same spot
Use duty_limit with run_until_stalled so you don't strain the motor or the model.
Move the arm while driving using wait=False to save time (see Section 4).
Color sensor
Use a test print to learn what your sensor sees: add print(sensor.color(), sensor.reflection()) in the loop and watch the terminal.
Hold the LEGO piece at the same distance every time — a few millimeters from the sensor works best.
Pick clearly different colors. Red, white, and blue are easy to tell apart. Avoid pairs like red and orange.
Watch the hub light. It shows the color the robot sees. Only press the button when the light is the right color.
Code organization
One function per run. Keep each run short and focused.
Write helper functions for things you do often, like squaring up or zeroing an arm.
Use clear names. drive_base.straight(300) is fine, but a comment like # drive to the bridge helps teammates understand it.
Never delete a working run without saving a copy. Use Git commits so you can always go back.
Debugging
Read the error message. The line number tells you where to look.
Add print() lines to see values while the program runs.
Use beeps or display icons to see which part of a run is running when you aren't connected to a laptop: hub.display.icon(Icon.UP).
9. Common Mistakes
Mistake	Wrong	Right
Missing def	left_run1():	def left_run1():
Name doesn't match the call	defined left1_run, called left_run1()	Use the same name in both places
Wrong color case	Color.Red	Color.RED
Mixed if / elif	if ... if ... elif ...	if ... elif ... elif ...
Function used before it's defined	calling main() above the run functions	Put all defs first, main() last
Bad indentation	mixing tabs and spaces	Use 4 spaces for every level
Wrong units	drive_base.straight(30) meaning 30 cm	drive_base.straight(300) (mm)
Button held too long	one press starts two runs	Wait for release before starting a run
10. Documenting Your Work

Good documentation helps your team, and judges in the Robot Design interview love to see it. Follow these steps every time you change the code.

Step 1: Comment the top of each run
python
def right_run2():
    # Mission:        M05 — Example Mission
    # Start position: right home, 2 grid squares from the wall, using jig B
    # Attachment:     hook on the right tool motor
    # Points:         20
    # Success rate:   9/10 (tested 2026-11-04)
Step 2: Keep a change log

Add an entry to CHANGELOG.md (or the section below) each practice:

## 2026-11-04
- left_run1: increased first straight from 380 to 400 mm (was stopping short)
- right_run2: new run for M05, 9/10 success
- Who: Ava, Leo
Step 3: Commit with a clear message

If you use Git:

Save your changes in Pybricks Code and export main.py into this repository folder.
Stage the file: git add main.py
Commit with a message that says what and why: git commit -m "left_run1: longer first drive so robot reaches the model"
Push to share it: git push
Step 4: Record test results

Track how reliable each run is. It shows which runs need work.

Run	Date	Attempts	Successes	Notes
left_run1	2026-11-04	10	9	One miss from crooked start
Step 5: Take photos or videos

Save pictures of attachments and short videos of runs in a docs/ folder. They help you rebuild if something breaks and give you material for the judging presentation.

11. Resources
Pybricks Code (editor): https://code.pybricks.com
Pybricks documentation: https://docs.pybricks.com
Pybricks main site: https://pybricks.com
FIRST LEGO League: https://www.firstlegoleague.org
Python basics: https://docs.python.org/3/tutorial/

Pybricks updates often. If a feature in this README doesn't work, check that your hub has the latest Pybricks firmware and compare with the official docs.
