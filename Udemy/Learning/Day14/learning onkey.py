from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.fd(50)


def move_backwards():
    tim.backward(50)


def move_left():
    tim.setheading(180)


def move_right():
    tim.setheading(0)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.exitonclick()
