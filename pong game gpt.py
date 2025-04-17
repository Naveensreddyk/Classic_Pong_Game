import turtle

# Screen setup
screen = turtle.Screen()
screen.title("Pong Game by Naveen")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Stops automatic screen updates for smoother animation

# Left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(40)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(40)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15  # Ball movement in x-direction
ball.dy = -0.15  # Ball movement in y-direction

# Score
score_a = 0
score_b = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions to move paddles
def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:  # Limit paddle movement
        left_paddle.sety(y + 20)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -240:
        left_paddle.sety(y - 20)

def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        right_paddle.sety(y + 20)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -240:
        right_paddle.sety(y - 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(left_paddle_up, "w")  # Left paddle moves up with 'w'
screen.onkeypress(left_paddle_down, "s")  # Left paddle moves down with 's'
screen.onkeypress(right_paddle_up, "Up")  # Right paddle moves up with 'Up Arrow'
screen.onkeypress(right_paddle_down, "Down")  # Right paddle moves down with 'Down Arrow'

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Collision with top wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverse direction

    # Collision with bottom wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Ball goes off screen (left side)
    if ball.xcor() < -390:
        score_b += 1
        score_display.clear()
        score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)  # Reset ball position
        ball.dx *= -1  # Reverse ball direction

    # Ball goes off screen (right side)
    if ball.xcor() > 390:
        score_a += 1
        score_display.clear()
        score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Ball collision with left paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1  # Reverse ball direction

    # Ball collision with right paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
