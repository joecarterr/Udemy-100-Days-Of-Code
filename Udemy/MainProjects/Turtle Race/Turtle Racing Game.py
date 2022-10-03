from turtle import Turtle, Screen
import random

# start race:
is_race_on = False

# startup:
screen = Screen()
# screen boundaries:
screen.setup(width=600, height=400)
# title:
screen.title("Turtle Race")
# turtle colours:
colours = ["red", "orange", "green", "blue", "purple", "violet"]
# background colour:
screen.bgcolor("light blue")
# making a bet:
user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will win the race? Enter it's colour")

# turtle positions:
y_positions = [-150, -100, -50, 0, 50, 100]

# all six turtles:
all_turtles = []

for turtle_index in range(0, 6):
    # turtle number one:
    turtles = Turtle(shape="turtle")
    turtles.shapesize(1.5)
    turtles.penup()
    turtles.color(colours[turtle_index])
    turtles.goto(x=-300, y=y_positions[turtle_index])
    all_turtles.append(turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! {winning_colour} won!")
                is_race_on = False
            else:
                print(f"Sorry you lost. {winning_colour} won.")
                is_race_on = False
        random_turtle_distance = random.randint(0, 10)
        turtle.fd(random_turtle_distance)

screen.exitonclick()
