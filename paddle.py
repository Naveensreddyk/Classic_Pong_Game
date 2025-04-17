from turtle import Turtle
class Paddle(Turtle): #Paddle class is created and the attributes are inherited from the Turtle class.
    def __init__(self, position): #passed position as the parameter and the parameters are passed in the main.py
    # created paddles with the turtle attributes.
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self): #Created a method for the paddles to move up.
        if self.ycor() < 245: #If the paddle's y-axis position is less than 245 then the paddle is allowed to move up.
            new_y = self.ycor() + 30 #If the paddle is moving up, It has to move 20 paces.
            self.goto(self.xcor(), new_y) #The paddle moves to the new y co-ordinate while keeping the x co-ordinate the same.

    def go_down(self):
        if self.ycor() > -230: #If the paddle's y-axis position is less than -230 then the paddle is allowed to move down.
            new_y = self.ycor() - 30 #If the paddle is moving down, It has to move 20 paces.
            self.goto(self.xcor(), new_y) #The paddle moves to the new y co-ordinate while keeping the x co-ordinate the same.

