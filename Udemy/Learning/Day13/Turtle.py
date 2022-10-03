from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pencolor("blue")


def draw_sides(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.fd(100)
        tim.right(angle)


for shape_side in range(1, 11):
    draw_sides(shape_side)

screen = Screen()
screen.exitonclick()
