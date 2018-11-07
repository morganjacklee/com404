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
        self.add_email_label()
        self.add_email_entry()
        self.add_subscribe_button()
        

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
    def add_email_label(self):

        # 1. create component object
        self.email_label = Label()
        self.email_label.place(x=100, y=140)
        # 2. style the component
        self.email_label.configure(font="Arial 10",
                                     text="Email:",
                                     )


    def add_email_entry(self):

        # 1. create component object
        self.email_entry = Entry()
        self.email_entry.place(x=160, y=140)
        # 2. style the component
        self.email_entry.configure(font="Arial 12",
                                   )                                     

    def add_subscribe_button(self):

        # 1. create component object
        self.subscribe_button = Button()
        self.subscribe_button.place(x=20, y=200)
        # 2. style the component
        self.subscribe_button.configure(font="Arial 18",
                                     text="                        Subscribe                       ",
                                     )
    
