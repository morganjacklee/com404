from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ball_image = PhotoImage(file="ball.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.ball_x_pos = 250
        self.ball_y_pos = 25
        self.ball_x_change = 10
        self.ball_y_change = 10
        
        self.ball_x_pos_two = 0
        self.ball_y_pos_two = 120
        self.ball_x_change_two = 10
        self.ball_y_change_two = 10
        
        # add components
        self.add_ball_image_label()
        self.add_ball_image_label_two() 
        
        # start the timer
        self.tick()
        self.tick_two()
        
    # the timer tick function    
    def tick(self):
        self.ball_x_pos = self.ball_x_pos + self.ball_x_change
        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        

        # right
        if self.ball_x_pos >= 380:
            self.ball_x_change = -self.ball_x_change

        # left
        if self.ball_x_pos <= 0:
            self.ball_x_change = -self.ball_x_change

        # top
        if self.ball_y_pos <= 0:
            self.ball_y_change = -self.ball_y_change

        #bottom
        if self.ball_y_pos >= 380:
            self.ball_y_change = -self.ball_y_change

        self.after(100, self.tick)

    def tick_two(self):
        self.ball_x_pos_two = self.ball_x_pos_two + self.ball_x_change_two
        self.ball_y_pos_two = self.ball_y_pos_two + self.ball_y_change_two
        self.ball_image_label_two.place(x=self.ball_x_pos_two, 
                                    y=self.ball_y_pos_two)
        

        # right
        if self.ball_x_pos_two >= 380:
            self.ball_x_change_two = -self.ball_x_change_two

        # left
        if self.ball_x_pos_two <= 0:
            self.ball_x_change_two = -self.ball_x_change_two

        # top
        if self.ball_y_pos_two >= 0:
            self.ball_y_change_two = -self.ball_y_change_two

        #bottom
        if self.ball_y_pos_two <= 380:
            self.ball_y_change_two = -self.ball_y_change_two

        self.after(100, self.tick_two)


    # the ball image
    def add_ball_image_label(self):
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos,
                                    y=self.ball_y_pos)
        self.ball_image_label.configure(image=self.ball_image)

    def add_ball_image_label_two(self):
        self.ball_image_label_two = Label()
        self.ball_image_label_two.place(x=self.ball_x_pos_two,
                                    y=self.ball_y_pos_two)
        self.ball_image_label_two.configure(image=self.ball_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop()
