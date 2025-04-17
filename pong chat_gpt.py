from turtle import Turtle, Screen
import time
import random

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("🔥 Ultimate Animated Pong by Naveen 🔥")
screen.tracer(0)

# Draw Center Circle
circle = Turtle()
circle.color("white")
circle.penup()
circle.goto(0, -100)
circle.pendown()
circle.circle(100)
circle.hideturtle()

# Draw Center Dashed Line
line = Turtle()
line.color("white")
line.penup()
line.goto(0, 300)
line.setheading(270)

for _ in range(15):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)

line.hideturtle()

# Create Paddles
def create_paddle(x, y):
    paddle = Turtle()
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x, y)
    return paddle

right_paddle = create_paddle(350, 0)
left_paddle = create_paddle(-350, 0)

# Ball
ball = Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball_dx = 2
ball_dy = 2
speed_factor = 1.0

# Score
right_score = 0
left_score = 0
score_display = Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)

def update_score():
    score_display.clear()
    score_display.write(f"{left_score}  |  {right_score}", align="center", font=("Courier", 24, "bold"))

update_score()

# Paddle Movement
def right_paddle_up():
    if right_paddle.ycor() < 250:
        right_paddle.sety(right_paddle.ycor() + 30)

def right_paddle_down():
    if right_paddle.ycor() > -240:
        right_paddle.sety(right_paddle.ycor() - 30)

screen.listen()
screen.onkeypress(right_paddle_up, "Up")
screen.onkeypress(right_paddle_down, "Down")

# Power-ups
def random_power_up():
    global speed_factor
    power = random.choice(["speed_boost", "shrink_paddle", "grow_paddle", None])
    if power == "speed_boost":
        speed_factor *= 1.2
    elif power == "shrink_paddle":
        right_paddle.shapesize(stretch_wid=3, stretch_len=1)
    elif power == "grow_paddle":
        right_paddle.shapesize(stretch_wid=7, stretch_len=1)

# AI-controlled Left Paddle
def move_left_paddle():
    if left_paddle.ycor() < ball.ycor():
        left_paddle.sety(left_paddle.ycor() + 2 * speed_factor)
    elif left_paddle.ycor() > ball.ycor():
        left_paddle.sety(left_paddle.ycor() - 2 * speed_factor)

# Winning Condition
def check_winner():
    global game_on
    if left_score == 10:
        score_display.goto(0, 0)
        score_display.write("🔥 LEFT PLAYER WINS! 🔥", align="center", font=("Courier", 24, "bold"))
        game_on = False
    elif right_score == 10:
        score_display.goto(0, 0)
        score_display.write("🔥 RIGHT PLAYER WINS! 🔥", align="center", font=("Courier", 24, "bold"))
        game_on = False

# Game Loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.01)

    # Move Ball
    ball.setx(ball.xcor() + (ball_dx * speed_factor))
    ball.sety(ball.ycor() + (ball_dy * speed_factor))

    # Ball collision with walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball_dy *= -1

    # Move AI Paddle
    move_left_paddle()

    # Ball collision with paddles
    if (ball.xcor() > 340 and ball.distance(right_paddle) < 50) or (ball.xcor() < -340 and ball.distance(left_paddle) < 50):
        ball_dx *= -1.1  # Increase speed each hit
        speed_factor *= 1.05  # Game gets harder
        random_power_up()

    # Ball out of bounds (score update)
    if ball.xcor() > 390:
        left_score += 1
        update_score()
        ball.goto(0, 0)
        ball_dx = -2
        speed_factor = 1.0

    if ball.xcor() < -390:
        right_score += 1
        update_score()
        ball.goto(0, 0)
        ball_dx = 2
        speed_factor = 1.0

    check_winner()

screen.exitonclick()
