from turtle import Turtle


class Ball(Turtle): #Created a ball class and the attributes are inherited from the Turtle class.

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(1)
        self.penup()
        self.x_move = 10 #ball to be moved in the x co-ordinate with a speed of 10.
        self.y_move = 10  #ball to be moved in the y co-ordinate with a speed of 10.
        self.move_speed = 0.1 #here move speed is set to 0.1.

    def move(self): #Created a move method to move the ball
        new_x = self.xcor() + self.x_move #new_x variable is created and x_move which is 10 paces added to the current x cor to make the ball move.
        new_y = self.ycor() + self.y_move #new_y variable is created and y_move which is 10 paces added to the current y cor to make the ball move.
        self.goto(new_x, new_y) #now the ball go to the new position.


    def bounce_y(self): #bounce method is created
        #Multiplying with -1 it reverses its direction.
        self.y_move *= -1 #This method makes the ball bounce vertically by reversing the direction of the vertical movement.

    def bounce_x(self): #This method makes the ball bounce horizontally by reversing the direction of its horizontal movement.
        self.x_move *= -1 #Multiplying with -1 reverses the direction.
        self.move_speed *= 0.9 #reduces its speed by 10 percent after every bounce.

    def reset_position(self): #This method resets ball position to the center of the screen.
        self.goto(0,0) #sets the position to (0,0).
        self.move_speed = 0.1 #sets to the ball to the original speed.
        self.bounce_x() #its start moving in a new direction after resetting.