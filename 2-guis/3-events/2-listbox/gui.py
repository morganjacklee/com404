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
                   width=700,
                       )

        
        
        

        # add components/widgets
        self.add_program_frame()
        
        self.add_heading_label()
        self.add_center_label()
        self.add_lyric_frame()
        
        self.add_lyric_entry()
        self.add_add_button()
        self.add_lyric_result_label()
        self.add_lyric_options_list()
        


    def add_program_frame(self):
        self.program_frame = Frame()
        self.program_frame.grid()
        self.program_frame.configure(bg="#FEE")
        
        

    def add_lyric_frame(self):
        self.lyric_frame = Frame(self.program_frame)
        self.lyric_frame.grid()
        

    def add_heading_label(self):

        # 1. create component object
        self.heading_label = Label(self.program_frame)
        self.heading_label.grid(row=0, column =0, sticky=N)
        # 2. style the component
        self.heading_label.configure(font="Arial 24",
                                     text="Song Maker",
                                     )

    def add_center_label(self):

        # 1. create component object
        self.center_label = Label(self.program_frame)
        self.center_label.grid(row=1, column =0, sticky=W)
        # 2. style the component
        self.center_label.configure(font="Arial 10",
                                     text="Lyric to add:",
                                     )


    def add_lyric_entry(self):

        # 1. create component object
        self.lyric_entry = Entry(self.lyric_frame)
        self.lyric_entry.grid(row=2, column =0, sticky=W)
        # 2. style the component
        self.lyric_entry.configure(font="Arial 12",
                                   )                                     

    def add_add_button(self):

        # 1. create component object
        self.add_button = Button(self.lyric_frame)
        self.add_button.grid(row=2, column =2, sticky=N)
        # 2. style the component
        self.add_button.configure(font="Arial 8",
                                        text="ADD")
        self.add_button.bind("<ButtonRelease-1>", self.button_clicked)

    def add_lyric_result_label(self):

        # 1. create component object
        self.lyric_result_label = Label(self.program_frame)
        self.lyric_result_label.grid(row=4, column =0, sticky=W)
        # 2. style the component
        self.lyric_result_label.configure(font="Arial 10",
                                     text="Lyrics:",
                                     )

    def add_lyric_options_list(self):

        # 1. create component object
        self.lyric_options_list = Listbox(self.program_frame)
        self.lyric_options_list.grid(row=5, column =0, sticky=W)
        # 2. style the component


    def button_clicked(self,event):
        lyric = self.lyric_entry.get()
        self.lyric_options_list.insert(END, lyric)

