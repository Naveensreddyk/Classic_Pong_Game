from turtle import Turtle


class Design(Turtle): #Ceated a class Design and the attributes are inherited form the turtle class.
    def __init__(self):
        super().__init__()
        # created a circle in the middle of the board for the design purposes.
        self.color("white")
        self.penup()
        self.goto(0, -50)
        self.pendown()
        self.pensize(3)
        self.circle(50)
        self.hideturtle()
#Created a center line in the middle of the board
    def center_line(self):
        self.color("white")
        self.penup()
        self.pensize(3)
        self.goto(0, 300)
        self.pendown()
        self.goto(0, -300)