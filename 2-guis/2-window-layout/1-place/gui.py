from tkinter import * 

class Gui(Tk):
    # initialise the object
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Newsletter")
        self.configure(bg="#C0C0C0",
                   height=300, 
                   width=500)

        # add components/widgets
        self.add_heading_label()
        self.add_center_label()

    def add_heading_label(self):

        # 1. create component object
        self.heading_label = Label()
        self.heading_label.place(x=20, y=20)
        # 2. style the component
        self.heading_label.configure(font="Arial 24",
                                     text="RECEIVE OUR NEWSLETTER",
                                     )

    def add_center_label(self):

        # 1. create component object
        self.center_label = Label()
        self.center_label.place(x=40, y=80)
        # 2. style the component
        self.center_label.configure(font="Arial 12",
                                     text="Please enter your email below to receive our newsletter.",
                                     )
