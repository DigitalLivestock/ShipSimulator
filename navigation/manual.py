import _thread as thread
from tkinter import *
from time import sleep

panel_size_x = 300
panel_size_y =  120
zoom = 35

class Manual:
    def __init__(self):
        self.throttle = 0
        self.rudder = 0
        self.update_thread = 0
        self.root = None
        self.mainframe = None
        self.canvas = None
        self.button_left = None
        self.button_right = None

    def get_throttle(self):
        return self.throttle

    def get_rudder(self):
        return self.rudder

    def inc_left(self):
        self.rudder += 4

    def inc_right(self):
        self.rudder -= 4

    def throttle_inc(self):
        self.throttle += 1

    def throttle_dec(self):
        self.throttle -= 1

    def panel(self):
        self.root = Tk()

        self.root.title("Control panel:")

        self.mainframe = Frame(self.root, width = str(panel_size_x), height = str(panel_size_y))
        self.mainframe.pack()

        self.button_left = Button(self.mainframe, text="Left", fg="blue", command=self.inc_left)
        self.button_left.pack(side=LEFT)

        self.button_right = Button(self.mainframe, text="Right", fg="yellow", command=self.inc_right)
        self.button_right.pack(side=RIGHT)

        self.button_up = Button(self.mainframe, text="INC THROTTLE", fg="green", command=self.throttle_inc)
        self.button_up.pack()

        self.button_down = Button(self.mainframe, text="DEC THROTTLE", fg="red", command=self.throttle_dec)
        self.button_down.pack()

        self.result = Label(self.mainframe, text=str(self.throttle))
        self.result.pack()
        
        def count():
            self.result.config(text=str(self.throttle))
            self.result.after(100, count)
        count()

        self.root.mainloop()

    def start_panel(self):
        self.update_thread = thread.start_new_thread(self.panel, ())
        print("Manual.start_panel: starting thread panel")

if "__main__" == __name__:
    manual = Manual()
    manual.start_panel()
    for i in range(5):
        sleep(1)
