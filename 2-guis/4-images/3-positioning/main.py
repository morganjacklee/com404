from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.map_image = PhotoImage(file="map.gif")
        self.bus_image = PhotoImage(file="bus.gif")
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_map_frame()
        self.add_heading_label()
        self.add_map_image_label()
        self.add_bus_image_label()
        self.add_heading_label()
        

    def add_map_frame(self):
        self.map_frame = Frame(width=400, height=400)
        self.map_frame.place(x=0, y=0)

    def add_map_image_label(self):
        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0, y=0)
        self.map_image_label.configure(image=self.map_image)
        
    def add_bus_image_label(self):
        self.bus_image_label = Label(self.map_frame)
        self.bus_image_label.place(x=10, y=10)
        self.bus_image_label.configure(image=self.bus_image)
        self.bus_image_label.bind("<B1-Motion>", self.left_clicked)
        
    def add_heading_label(self):

        # 1. create component object
        self.heading_label = Label()
        self.heading_label.place(x=30, y=0)
        # 2. style the component
        self.heading_label.configure(font="Arial 10",
                                     text="Bus Journey",
                                     )

    

    #def bus_move(self):
        #messagebox.showinfo("Bus Journey Gui", "Mouse x is" + str(event.x))
        #messagebox.showinfo("Bus Journey Gui", "Mouse y is" + str(event.y))
        

    def left_clicked(self,event):
        first = event.x
        second = event.y
        self.bus_image_label.place(x=first,y=second)
         

        
        


    

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
