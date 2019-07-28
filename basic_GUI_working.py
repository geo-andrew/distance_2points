import tkinter # the GUI toolbox
import functools  # partial function allows import of more than one peramater per button
import pyproj


root = tkinter.Tk()  # must match the bottom two lines of code in order for this to work


class Window(tkinter.Frame):

    def click_quit(self):
        print("The user clicked 'cancel'")
        self.master.destroy()

    

    def click_enter(self, p1lat, p1long, p2lat, p2long):

        print(p1lat, p1long, p2lat, p2long)
        self.master.destroy()

    def __init__(self, master=None):

        tkinter.Frame.__init__(self, master)

        self.master = master

        self.init_window()

        self.pack()

    def init_window(self):

        # The GUI can be dragged larger or smaller horizontally or vertically, True for resizable, False for fixed
        self.master.resizable(True, True)

        title_font = ('Arial', 16)

        font = ('Arial', 10)

        # Improved color
        self.master.tk_setPalette(background='#ececec')

        # Title
        self.master.title("Distance calculator")

        # Positions the GUI in the screen sweet spot

        x = (self.master.winfo_screenwidth() -
             self.master.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() -
             self.master.winfo_reqheight()) / 3
        x = str(int(x))
        y = str(int(y))
        self.master.geometry("+{}+{}". format(x, y))

        
        # Title
        title = tkinter.Label(self, text = "App for finding the distance between two points.", font = title_font)
        # explanation text for GUI
        text1 = tkinter.Label(self, text="Please exter the X and Y coordinates of two points.", font = font)
        # explanation text for GUI
        text2 = tkinter.Label(self, text = "Characters other than the numbers 0 - 9\nand . will not be accepted.", font = font)
        # labels for input boxes

        input_frame = tkinter.Frame(self)
        input_frame.grid(row = 4)

        # Labels for input boxes
        label1 = tkinter.Label(input_frame, text="Latitude of point 1", font=font)
        label2 = tkinter.Label(input_frame, text="Longitude of point 1", font=font)
        label3 = tkinter.Label(input_frame, text="Latitude of point 2", font=font)
        label4 = tkinter.Label(input_frame, text="Longitude of point 2", font=font)

        # The names of the four variables to be input, allows floats to deal with lat and long
        # the latitude of point 1
        p1lat = tkinter.Spinbox(input_frame, from_=-90.0, to=90.0)
        # the longitude of point 1
        p1long = tkinter.Spinbox(input_frame, from_=-180.0, to=180.0)
        # the latitude of point 2
        p2lat = tkinter.Spinbox(input_frame, from_=-90.0, to=90.0)
        # the longitude of point 2
        p2long = tkinter.Spinbox(input_frame, from_=-180.0, to=180.0)

        # positioning of title text
        title.grid(row=0, padx=10, pady=10)
        # positioning of two portions of explanatory text
        text1.grid(row=1, padx=10, pady=10)
        text2.grid(row=2, padx=10, pady=10)

        # positioning of input labels and boxes
        label1.grid(row=0, column=0, padx=(20, 0), pady=10)
        p1lat.grid(row=0, column=1, padx=(0, 20), pady=10)
        label2.grid(row=1, column=0, padx=(20, 0), pady=10)
        p1long.grid(row=1, column=1, padx=(0, 20), pady=10)
        label3.grid(row=2, column=0, padx=(20, 0), pady=10)
        p2lat.grid(row=2, column=1, padx=(0, 20), pady=10)
        label4.grid(row=3, column=0, padx=(20, 0), pady=10)
        p2long.grid(row=3, column=1, padx=(0, 20), pady=10)

        button_frame = tkinter.Frame(self)
        button_frame.grid(row = 5)

        button1 = tkinter.Button(button_frame, text="Calculate distance", default='active',
                         command=functools.partial(self.click_enter, p1lat, p1long, p2lat, p2long))  # Variables are being attached to click_enter
        # variables come from the entry boxes and are passed into another function, click_enter(self)
        button2 = tkinter.Button(button_frame, text="Cancel", command=self.click_quit)

        button1.grid(row=0, column=0, sticky='e', padx=20, pady=(5, 10))
        button2.grid(row=0, column=1, sticky='w', padx=20, pady=(5, 10))

        results_frame = tkinter.Frame(self)
        results_frame.grid(row = 6)

        # Result label
        result_label1 = tkinter.Label(results_frame, text="The distance between the two points you entered is: ", font=font)
        result_label2 = tkinter.Label(results_frame, text=" units", font=font)
        # box for calculated distance
        distance_output = tkinter.Text(results_frame, width = 5, height = 1, background = "light grey")


        # positioning the results output label 1
        result_label1.grid(row=0, column=0, padx=(10, 0), pady=10)
        
        # positioning the calculated distance box
        distance_output.grid(row = 0, column = 1)

        # positioning the results output label 2
        result_label2.grid(row=0, column=2, padx=(0, 10), pady=10)

        # menu
        menu = tkinter.Menu(self.master)
        self.master.config(menu=menu)

        # file cascade
        file = tkinter.Menu(menu)

        file.add_command(label='Exit', command=self.click_quit)


app = Window(root)

root.mainloop()

