from turtle import Turtle, Screen

arrow = Turtle()
screen = Screen()
arrow.color("gray")
arrow.pensize(3)

def move_forwards():
    arrow.fd(30)


def move_backwards():
    arrow.bk(30)


def move_left():
    new_heading = arrow.heading() + 10
    arrow.setheading(new_heading)


def move_right():
    new_heading = arrow.heading() - 10
    arrow.setheading(new_heading)


def pen_up():
    arrow.penup()


def pen_down():
    arrow.pendown()


def clear():
    arrow.clear()
    arrow.penup()
    arrow.home()
    arrow.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="q", fun=pen_up)
screen.onkey(key="e", fun=pen_down)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
