import serial.tools.list_ports
from tkinter import *
from pyfirmata import SERVO, Arduino
import threading
from threading import Event

# Search for COM port w/ Arduino and connect to that port
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "Arduino" in p.description:
        board = Arduino(p.device)
        print(p.device, p.description)
        break
    else:
        print("Cannot find Arduino in COM port")

# Set up pins for servos
board.digital[2].mode = SERVO
board.digital[3].mode = SERVO
board.digital[4].mode = SERVO
board.digital[5].mode = SERVO
board.digital[6].mode = SERVO
board.digital[7].mode = SERVO

# Set pin 8 to receive Demon TTL input for autorun function. Demon_pin.write(1) to start, Demon_pin.write(0) to stop
# Demon_pin = board.digital[8]

# Create variables for servos as digital outputs
servo1 = board.get_pin('d:2:o')
servo2 = board.get_pin('d:3:o')
servo3 = board.get_pin('d:4:o')
servo4 = board.get_pin('d:5:o')
servo5 = board.get_pin('d:6:o')
servo6 = board.get_pin('d:7:o')


# Define Knob class
class Knob(object):
    def __init__(self, color, servo, off_img, run_img, open_img):
        self.color = color
        self.servo = servo
        self.off_img = off_img
        self.run_img = run_img
        self.open_img = open_img

    def off(self):
        if self.servo == servo1:
            servo1.write(2)
        elif self.servo == servo2:
            servo2.write(2)
        elif self.servo == servo3:
            servo3.write(2)
        elif self.servo == servo4:
            servo4.write(2)
        elif self.servo == servo5:
            servo5.write(2)
        elif self.servo == servo6:
            servo6.write(2)

    def run(self):
        if self.servo == servo1:
            servo1.write(65)
        elif self.servo == servo2:
            servo2.write(65)
        elif self.servo == servo3:
            servo3.write(65)
        elif self.servo == servo4:
            servo4.write(65)
        elif self.servo == servo5:
            servo5.write(65)
        elif self.servo == servo6:
            servo6.write(65)

    def open(self):
        if self.servo == servo1:
            servo1.write(130)
        elif self.servo == servo2:
            servo2.write(130)
        elif self.servo == servo3:
            servo3.write(130)
        elif self.servo == servo4:
            servo4.write(130)
        elif self.servo == servo5:
            servo5.write(130)
        elif self.servo == servo6:
            servo6.write(130)


# Defining knobs as class objects
pink = Knob('palevioletred2', servo1, "T:/Neurobiology-EspanaLab/Illustrations/pinkknob.png",
            'T:/Neurobiology-EspanaLab/Illustrations/pinkknob2.png',
            'T:/Neurobiology-EspanaLab/Illustrations/pinkknob3.png')

green = Knob('green4', servo2, "T:/Neurobiology-EspanaLab/Illustrations/greenknob.png",
             'T:/Neurobiology-EspanaLab/Illustrations/greenknob2.png',
             'T:/Neurobiology-EspanaLab/Illustrations/greenknob3.png')

yellow = Knob('yellow', servo3, 'T:/Neurobiology-EspanaLab/Illustrations/yellowknob.png',
              'T:/Neurobiology-EspanaLab/Illustrations/yellowknob2.png',
              'T:/Neurobiology-EspanaLab/Illustrations/yellowknob3.png')

red = Knob('red', servo4, 'T:/Neurobiology-EspanaLab/Illustrations/redknob.png',
           'T:/Neurobiology-EspanaLab/Illustrations/redknob2.png',
           'T:/Neurobiology-EspanaLab/Illustrations/redknob3.png')

white = Knob('white', servo5, 'T:/Neurobiology-EspanaLab/Illustrations/whiteknob.png',
             'T:/Neurobiology-EspanaLab/Illustrations/whiteknob2.png',
             'T:/Neurobiology-EspanaLab/Illustrations/whiteknob3.png')

blue = Knob('deepskyblue', servo6, 'T:/Neurobiology-EspanaLab/Illustrations/blueknob.png',
            'T:/Neurobiology-EspanaLab/Illustrations/blueknob2.png',
            'T:/Neurobiology-EspanaLab/Illustrations/blueknob3.png')

# Set up GUI and define the functions controlled by various buttons
window = Tk()
window.geometry("400x650")
window.title("Knob Control Program")

title = Label(window, text="Welcome to Knobby", relief='solid', font=("arial", 16, "bold")).pack()
status_window = Label(window, text='Ready', font=("arial", 10, "bold"), relief=SUNKEN)
status_window.place(x=15, y=10)
status_window.config(height=2, width=7)

# Calling exit.set() stops the autorun thread. It is the only method I found that allows GUI input while a
# threaded loop is running
exit = Event()


def stop():
    exit.set()


# This counts up to 7 files for each concentration. To match Demon, 1st 30s = data collection, subsequent 150s = wait
# period with new file name.
def file_counter():
    for i in range(1, 8):
        status_window.config(text=f'File {i}')
        exit.wait(30)
        if not i == 7:
            status_window.config(text=f'File {i+1}')
            exit.wait(151)

# Threaded autorun function. Can only be started once. Must exit and restart program to rerun this function.
# Checks value of checkbox prior to starting each concentration
def autorun():
    exit.clear()
    stop_b.config(relief=SUNKEN, bg="red2")
    autorun_b.config(text='Running', fg='green', relief=SUNKEN)
    status_window.config(text='File 0', fg='black')
    if pink_check.var.get() == 1:
        pink.run()
        status_window.config(bg=pink.color)
        file_counter()
    if green_check.var.get() == 1:
        green.run()
        status_window.config(bg=green.color)
        file_counter()
    if yellow_check.var.get() == 1:
        yellow.run()
        status_window.config(bg=yellow.color)
        file_counter()
    if red_check.var.get() == 1:
        red.run()
        status_window.config(bg=red.color)
        file_counter()
    if white_check.var.get() == 1:
        white.run()
        status_window.config(bg=white.color)
        file_counter()
    if blue_check.var.get() == 1:
        blue.run()
        status_window.config(bg=blue.color)
        file_counter()
    autorun_b.config(relief=SUNKEN, bg="SystemButtonFace", text='Run Complete', fg='black')
    stop_b.config(relief=RAISED, bg="SystemButtonFace")
    if exit.is_set():
        autorun_b.config(text='Run Stopped', fg='red', relief=SUNKEN)
        stop_b.config(relief=RAISED, bg="SystemButtonFace")
        status_window.config(bg='SystemButtonFace', text='Stopped')


# Threads the autorun function so it can run concurrently w/ tkinter window
t1 = threading.Thread(target=autorun)
t1.isDaemon()


# starts autorun thread
def startup():
    t1.start()


autorun_b = Button(window, text="AutoRun", relief=RAISED, font=("arial", 10, "bold"))
autorun_b.place(x=105, y=35)
autorun_b.config(command=startup, height=2, width=12)

stop_b = Button(window, text="STOP", relief=RAISED, font=("arial", 10, "bold"))
stop_b.place(x=220, y=35)
stop_b.config(command=stop, height=2, width=6)

# pink knob
pink_label = Entry(window, textvariable=StringVar(value='N/A'), bg=pink.color, relief=RAISED, font='large_font')
pink_label.place(x=15, y=111)
pink_label.config(width=6)

p = IntVar(value=0)
pink_check = Checkbutton(window, text='Run', variable=p)
pink_check.place(x=20, y=135)
pink_check.var = p

pink_off_img = PhotoImage(file=pink.off_img)
pink_off_b = Button(window, image=pink_off_img, command=pink.off)
pink_off_b.place(x=85, y=100)
pink_off_b.config(height=60, width=80)

pink_run_img = PhotoImage(file=pink.run_img)
pink_run_b = Button(window, image=pink_run_img, command=pink.run)
pink_run_b.place(x=190, y=100)
pink_run_b.config(height=60, width=80)

pink_open_img = PhotoImage(file=pink.open_img)
pink_open_b = Button(window, image=pink_open_img, command=pink.open)
pink_open_b.place(x=295, y=100)
pink_open_b.config(height=60, width=80)

# green knob
green_label = Entry(window, textvariable=StringVar(value=".3 coc"), bg=green.color, relief=RAISED, font='large_font')
green_label.place(x=15, y=201)
green_label.config(width=6)

g = IntVar(value=1)
green_check = Checkbutton(window, text='Run', variable=g)
green_check.place(x=20, y=225)
green_check.var = g

green_off_img = PhotoImage(file=green.off_img)
green_off_b = Button(window, image=green_off_img, command=green.off)
green_off_b.place(x=85, y=190)
green_off_b.config(height=60, width=80)

green_run_img = PhotoImage(file=green.run_img)
green_run_b = Button(window, image=green_run_img, command=green.run)
green_run_b.place(x=190, y=190)
green_run_b.config(height=60, width=80)

green_open_img = PhotoImage(file=green.open_img)
green_open_b = Button(window, image=green_open_img, command=green.open)
green_open_b.place(x=295, y=190)
green_open_b.config(height=60, width=80)

# yellow knob
yellow_label = Entry(window, textvariable=StringVar(value="1 coc"), bg=yellow.color, relief=RAISED, font='large_font')
yellow_label.place(x=15, y=291)
yellow_label.config(width=6)

y = IntVar(value=1)
yellow_check = Checkbutton(window, text='Run', variable=y)
yellow_check.place(x=20, y=315)
yellow_check.var = y

yellow_off_img = PhotoImage(file=yellow.off_img)
yellow_off_b = Button(window, image=yellow_off_img, command=yellow.off)
yellow_off_b.place(x=85, y=280)
yellow_off_b.config(height=60, width=80)

yellow_run_img = PhotoImage(file=yellow.run_img)
yellow_run_b = Button(window, image=yellow_run_img, command=yellow.run)
yellow_run_b.place(x=190, y=280)
yellow_run_b.config(height=60, width=80)

yellow_open_img = PhotoImage(file=yellow.open_img)
yellow_open_b = Button(window, image=yellow_open_img, command=yellow.open)
yellow_open_b.place(x=295, y=280)
yellow_open_b.config(height=60, width=80)

# red knob
red_label = Entry(window, textvariable=StringVar(value="3 coc"), bg=red.color, relief=RAISED, font='large_font')
red_label.place(x=15, y=381)
red_label.config(width=6)

r = IntVar(value=1)
red_check = Checkbutton(window, text='Run', variable=r)
red_check.place(x=20, y=405)
red_check.var = r

red_off_img = PhotoImage(file=red.off_img)
red_off_b = Button(window, image=red_off_img, command=red.off)
red_off_b.place(x=85, y=370)
red_off_b.config(height=60, width=80)

red_run_img = PhotoImage(file=red.run_img)
red_run_b = Button(window, image=red_run_img, command=red.run)
red_run_b.place(x=190, y=370)
red_run_b.config(height=60, width=80)

red_open_img = PhotoImage(file=red.open_img)
red_open_b = Button(window, image=red_open_img, command=red.open)
red_open_b.place(x=295, y=370)
red_open_b.config(height=60, width=80)

# white knob
white_label = Entry(window, textvariable=StringVar(value="10 coc"), bg=white.color, relief=RAISED, font='large_font')
white_label.place(x=15, y=471)
white_label.config(width=6)

w = IntVar(value=1)
white_check = Checkbutton(window, text='Run', variable=w)
white_check.place(x=20, y=495)
white_check.var = w

white_off_img = PhotoImage(file=white.off_img)
white_off_b = Button(window, image=white_off_img, command=white.off)
white_off_b.place(x=85, y=460)
white_off_b.config(height=60, width=80)

white_run_img = PhotoImage(file=white.run_img)
white_run_b = Button(window, image=white_run_img, command=white.run)
white_run_b.place(x=190, y=460)
white_run_b.config(height=60, width=80)

white_open_img = PhotoImage(file=white.open_img)
white_open_b = Button(window, image=white_open_img, command=white.open)
white_open_b.place(x=295, y=460)
white_open_b.config(height=60, width=80)

# blue knob
blue_label = Entry(window, textvariable=StringVar(value="30 coc"), bg=blue.color, relief=RAISED, font='large_font')
blue_label.place(x=15, y=561)
blue_label.config(width=6)

b = IntVar(value=1)
blue_check = Checkbutton(window, text='Run', variable=b)
blue_check.place(x=20, y=585)
blue_check.var = b

blue_off_img = PhotoImage(file=blue.off_img)
blue_off_b = Button(window, image=blue_off_img, command=blue.off)
blue_off_b.place(x=85, y=550)
blue_off_b.config(height=60, width=80)

blue_run_img = PhotoImage(file=blue.run_img)
blue_run_b = Button(window, image=blue_run_img, command=blue.run)
blue_run_b.place(x=190, y=550)
blue_run_b.config(height=60, width=80)

blue_open_img = PhotoImage(file=blue.open_img)
blue_open_b = Button(window, image=blue_open_img, command=blue.open)
blue_open_b.place(x=295, y=550)
blue_open_b.config(height=60, width=80)

window.mainloop()
