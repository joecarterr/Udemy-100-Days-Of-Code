import turtle as t
import random

again = 0
tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.color("orange")
tim.pensize(3)
tim.speed('normal')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color(r, g, b)
    return random_color()


directions = [0, 90, 180, 360]
distance = [50, 60, 70, 80, 100, 150, 200]

for _ in range(1, 100):
    tim.color(random_color())
    tim.fd(random.choice(distance))
    tim.right(random.choice(directions))
