import time
from turtle import Screen, Turtle

from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

scoreboard = Turtle()
scoreboard.hideturtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.goto(0, 260)
left_score = 0
right_score = 0


def update_scoreboard():
    scoreboard.clear()
    scoreboard.write(
        f"{left_score}   {right_score}",
        align="center",
        font=("Courier", 24, "normal"),
    )


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

update_scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (
        ball.xcor() < -320 and ball.distance(l_paddle) < 50
    ):
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_position()
        left_score += 1
        update_scoreboard()

    if ball.xcor() < -390:
        ball.reset_position()
        right_score += 1
        update_scoreboard()

    screen.update()

screen.exitonclick()