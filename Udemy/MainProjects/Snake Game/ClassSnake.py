from turtle import Turtle

SNAKE_XPOSITIONS = [0, -20, -40]
# snakes moving distance:
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # create snake:
        for snakes in range(3):
            # snake shape:
            SNAKE = Turtle(shape="square")
            # stopping file from drawing a black line through the white square:
            SNAKE.penup()
            # snakes colour:
            SNAKE.color("white")
            # getting each square to go to a different position:
            SNAKE.goto(x=SNAKE_XPOSITIONS[snakes], y=0)
            # add to segments:
            self.segments.append(SNAKE)

    def move(self):
        # 1 - start = number you'd like to start on
        # 2 - stop = number you'd like to end on
        # 3 - step = number in which you'd like to go up or down by each time:
        # making the snake be able to move properly:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # X first, Y second:
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
