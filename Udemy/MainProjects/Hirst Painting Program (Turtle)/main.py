import random
from turtle import Screen, Turtle

dots = Turtle()
screen = Screen()
screen.colormode(255)
dots.speed("fastest")
dots.penup()
# getting the pen to go to the bottom right:
dots.setheading(225)
# moving it forward 300 paces to the bottom right:
dots.forward(300)
# once it reaches the bottom right turning it back straight:
dots.setheading(0)
dots.color("black")
screen.bgcolor("black")

WIDTH, HEIGHT = 600, 600
screen.setup(WIDTH, HEIGHT)

# random colors:
color_list = [(250, 246, 243), (211, 154, 98), (53, 107, 131), (235, 240, 244), (177, 78, 33),
              (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109),
              (12, 50, 64),
              (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79)]


# outputting the dots onto the screen:
for dot_count in range(1, 101):
    dots.dot(30, random.choice(color_list))
    dots.forward(50)

    if dot_count % 10 == 0:
        # 0 = back to straight
        # 90 = up
        # 180 = left
        # 270 = down
        # 360 = right
        # up:
        dots.setheading(90)
        dots.forward(50)
        # left:
        dots.setheading(180)
        # moving the dot to the start of a new line:
        dots.forward(500)
        dots.setheading(0)

screen.exitonclick()
