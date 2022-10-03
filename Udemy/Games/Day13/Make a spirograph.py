import random
import turtle

point = turtle.Turtle()
screen = turtle.Screen()
turtle.bgcolor("black")
turtle.colormode(255)

turtle.speed("fastest")


def random_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    color = (R, G, B)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.circle(140)
        turtle.color(random_color())
        current_heading = turtle.heading()
        turtle.setheading(current_heading + size_of_gap)


draw_spirograph(5)
screen.exitonclick()
