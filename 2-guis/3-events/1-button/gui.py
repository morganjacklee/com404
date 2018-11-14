from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    # initialise the object
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Newsletter")
        self.configure(bg="#C0C0C0",
                   height=300, 
                   width=500,
                       )

        
        
        

        # add components/widgets
        self.add_program_frame()
        
        self.add_heading_label()
        self.add_center_label()
        self.add_email_frame()
        self.add_email_label()
        self.add_email_entry()
        self.add_subscribe_button()
        


    def add_program_frame(self):
        self.program_frame = Frame()
        self.program_frame.pack(fill=X,padx=10, pady=10)
        self.program_frame.configure(bg="#FEE")
        
        

    def add_email_frame(self):
        self.email_frame = Frame(self.program_frame)
        self.email_frame.pack(fill=X,padx=10, pady=5)
        

    def add_heading_label(self):

        # 1. create component object
        self.heading_label = Label(self.program_frame)
        self.heading_label.pack(fill=X,side=TOP,padx=10, pady=10)
        # 2. style the component
        self.heading_label.configure(font="Arial 24",
                                     text="RECEIVE OUR NEWSLETTER",
                                     )

    def add_center_label(self):

        # 1. create component object
        self.center_label = Label(self.program_frame)
        self.center_label.pack(fill=X,padx=10, pady=20)
        # 2. style the component
        self.center_label.configure(font="Arial 12",
                                     text="Please enter your email below to receive our newsletter.",
                                     )
    def add_email_label(self):

        # 1. create component object
        self.email_label = Label(self.email_frame)
        self.email_label.pack(fill=X,side=LEFT,padx=10, pady=10)
        # 2. style the component
        self.email_label.configure(font="Arial 10",
                                     text="Email:",
                                     )


    def add_email_entry(self):

        # 1. create component object
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(fill=X,padx=10, pady=20)
        # 2. style the component
        self.email_entry.configure(font="Arial 12",
                                   )                                     

    def add_subscribe_button(self):

        # 1. create component object
        self.subscribe_button = Button(self.program_frame)
        self.subscribe_button.pack(fill=X,side=BOTTOM,padx=0, pady=0)
        # 2. style the component
        self.subscribe_button.configure(font="Arial 15",
                                        text="Subscribe")
        self.subscribe_button.bind("<ButtonRelease-1>", self.subscribe_clicked)

    def subscribe_clicked(self,event):
        email = self.email_entry.get()
        messagebox.showinfo("subscribtion Successful", "Thank you for subscribing! Your email: " + email + " has been registered for all future publications!")
