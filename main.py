from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
from scoreboard_design import Design

tim = Turtle()  #created a new object tim from turtle class to check the winner at the end.
tim.color("white") #got it the color white cause when the game_on condition fails it will display at the end.
tim.hideturtle() #It just hides the turtle.

screen = Screen()   #created a screen object from the Screen class
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("🥎PONG GAME by naveen 🔥") #Title which will be displayed on the top
screen.tracer(0)  #tracer will not show us what the turtle's been doing.

design = Design()  #created a design object form the Scoreboard Design class
design.center_line()    #called the center line method form the scoreboard design class.

r_paddle = Paddle((350, 0))   #created right paddle object from the Paddle class and passed the x and y co-ordinates as the parameters.
l_paddle = Paddle((-350, 0))  #created right paddle object from the Paddle class and passed the x and y co-ordinates as the parameters.

ball = Ball()    #crated ball object from the Ball class
scoreboard = Scoreboard()  #created a scoreboard object from the Scoreboard class.

screen.listen()  #screen listen is the method called from the screen class it will listen to the keystrokes entered by the user.
#given the functionalities to the keys and called the methods form the paddle
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

#While loop if the game os ON
game_on = True
while game_on:
    ball.move()  #called the method from the ball class to move the ball when the game is on.
    time.sleep(ball.move_speed) #added a time frame for the ball to move in a reasonable speed and move speed method is passed in as a parameter.
    screen.update() #Above we wrote the screen tracer(it will not show us what the turtle is doing). Now, the update method wil update with the final outcome.

#detecting the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280: #if the ball's y cor is more than 280(height of screen = 600) or less than then bounce method is called.
        ball.bounce_y()  #If the above condition passes then the ball bounce method is called.

#detecting the collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:  #width which is the x-axis = 800
        ball.bounce_x()  #If the above condition is passes then the ball bounce method is called.

#Checking if the ball misses the right paddle.
    if ball.xcor() > 390:   #If the ball x-axis position is more than 390 which way pass the right paddle.(width = 800)
        ball.reset_position() #If the above condition is passed then this method is called from the ball class
        scoreboard.l_point() #If the ball touches the wall passing the right paddle then the opponent gets a point.

#Checking if the ball misses the left paddle.
    if ball.xcor() < -390: #If the ball x-axis position is more than -390 which way passes tha left paddle.
        ball.reset_position() #we called the ball reset method from the ball class to reset the ball at the center.
        scoreboard.r_point()  #If the ball touches the wall passing the left paddle then the opponent gets a point.
#Checking the winner - Who gets the mark of 11 first they will be the winners.
    if scoreboard.l_score == 11: #If the score of the left player is equal to eleven.
        tim.goto(0, 0) #This is the new object for the display positioned at 0. depends on the winner it displays left or right.
        tim.write("🔥 LEFT PLAYER WINS! 🔥", align="center", font=("Courier", 24, "bold"))
        game_on = False #If the above condition is true then the game_on is False.
    elif scoreboard.r_score == 11: #If the right player score is equal to eleven.
        tim.goto(0, 0) #This is the new object for the display positioned at 0. depends on the winner it displays left or right.
        tim.write("🔥 RIGHT PLAYER WINS! 🔥", align="center", font=("Courier", 24, "bold"))
        game_on = False #If the above condition is true then the game_on is False.
screen.exitonclick()