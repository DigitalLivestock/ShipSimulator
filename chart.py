from tkinter import *
from time import sleep
import _thread as thread
from navigation.gps import *

map_size    = 800
zoom        = 15
oval_size   = 5

class Chart:
    def __init__(self):
        #Vectors to be drawn
        self.old_coordinates = (0, 0)
        #Thread ID
        self.update_thread = 0
        self.update_thread_2 = 0
        self.root = None
        self.canvas = None;
        self.mainframe = None


    def update_path(self, coordinates):
        while True:
            x = coordinates.get_x() * zoom + (map_size/2)
            y = coordinates.get_y() * zoom + (map_size/2)
            x_old = self.old_coordinates[0] + (map_size/2)
            y_old = self.old_coordinates[1] + (map_size/2)

            line = (x, y, x_old, y_old)
            self.old_coordinates = (x-(map_size/2), y-(map_size/2))
            self.canvas.create_line(line, fill="blue")
            self.canvas.create_oval(x+oval_size, y-oval_size, x-oval_size, y+oval_size, fill="red")
            sleep(0.5)
            self.canvas.update_idletasks() #not ideal

    def update_chart(self, coordinates):

        self.root = Tk()

        self.root.title("Chart:")
        #self.root.geometry("500x500")

        self.mainframe = Frame(self.root, width = str(map_size), height = str(map_size))
        self.mainframe.pack(expand=True, fill = BOTH)

        self.canvas = Canvas(self.mainframe, bg = "lightblue", width = str(map_size), height = str(map_size))
        self.canvas.pack(expand = True, fill = BOTH)

        self.root.after(1, self.start_update_path, coordinates)
        self.root.mainloop()

    def start_chart(self, coordinates):
        self.update_thread = thread.start_new_thread(self.update_chart, (coordinates,))
        print("Chart.start_chart: started thread with update_chart")

    def start_update_path(self, coordinates):
        self.update_thread_2 = thread.start_new_thread(self.update_path, (coordinates,))
        print("Chart.start_update_path: started thread with update_path")


if __name__ == "__main__":
    coordinates = gps()
    chart = Chart()
    chart.start_chart(coordinates)
    while True:
        continue
