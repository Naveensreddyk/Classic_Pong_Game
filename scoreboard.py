from turtle import Turtle

class Scoreboard(Turtle): #Created the class Scoreboard and the attributes are inherited form the Turtle class.
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard() #called the update score board method here

    def update_scoreboard(self):
        self.goto(-100, 250) #set the position for the score to display.
        self.write(self.l_score, align= "center", font=("Courier", 35, "normal"))
        self.goto(100, 250) #set the position for the score to display.
        self.write(self.r_score, align= "center", font=("Courier", 35, "normal"))

#Created methods to update the score by 1 each the opponent misses the ball. And update the score.
    def l_point(self):
        self.l_score += 1 #It will increase the score by 1.
        self.clear() #It will clear the screen of the old score.
        self.update_scoreboard() #It will update the scoreboard.

    def r_point(self):
        self.r_score += 1 #It will increase the score by 1.
        self.clear() #It will clear the screen of the old score.
        self.update_scoreboard() #It will update the scoreboard.









