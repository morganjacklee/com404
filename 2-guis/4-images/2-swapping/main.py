from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.left_image = PhotoImage(file="cactus1.gif")
        self.right_image = PhotoImage(file="cactus2.gif")
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_heading_label()
        self.add_left_button_label()
        self.add_flip_button()

    def add_left_button_label(self):
        self.left_button_label = Label()
        self.left_button_label.grid(row=1, column=1)
        self.left_button_label.configure(image=self.left_image,
                                             )

    def add_heading_label(self):

        # 1. create component object
        self.heading_label = Label()
        self.heading_label.grid(row=0, column =1, sticky=N)
        # 2. style the component
        self.heading_label.configure(font="Arial 24",
                                     text="Cactus Leaves",
                                     )
    def add_flip_button(self):
        self.flip_button = Button()
        self.flip_button.grid(row=2, column=1, sticky=S)
        self.flip_button.configure(font="Arial 15",
                                        text="FLIP")
        self.flip_button.bind("<ButtonRelease-1>", self.left_button_clicked)
        self.flip_button.bind("<ButtonRelease-3>", self.right_button_clicked)

    def right_button_clicked(self,event):
        self.left_button_label.configure(image = self.right_image)
    def left_button_clicked(self,event):
        self.left_button_label.configure(image = self.left_image)
    

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
