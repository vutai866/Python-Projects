# Pong game in Python3 

import turtle
import os

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(1) # Fastest 0, fast 10, normal 6, slow 3, slowest 1
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2 ## Set the ball moves by 2 pixel 
ball.dy = -2

# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0\tPlayer B: 0", align="center", font=("Courier", 24, "normal"))


# Function 
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding 
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
        # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 ## If the ball hit border, reverse the direction
        os.system("afplay bounce.mp3&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.mp3&") # afplay --> MAC, aplay --> Linux

        # Left and right
    if ball.xcor() > 350:
        ball.goto(0,0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}\tPlayer B: {scoreB}", align="center", font=("Courier", 24, "normal"))
        
    if ball.xcor() < -350:
        ball.goto(0,0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}\tPlayer B: {scoreB}", align="center", font=("Courier", 24, "normal"))
    
    # Paddle and ball collisions
    if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50\
    and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.mp3&") 

    elif ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50\
    and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.mp3&")