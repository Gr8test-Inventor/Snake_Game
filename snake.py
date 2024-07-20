from turtle import Turtle
#                       0         1         2
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
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
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(100, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # each segment(ex: 9,8,7,etc) starting from last seg in list (ex: 9)    start stop step (backwards) Ex: start: (last num in list) stop: 0 step: (last to first seg)
        for seg_num in range(len(self.segments) - 1, 0, -1): #Step is telling the computer how we're going to get there. (By going from the end of the list to the front.)
            new_x = self.segments[seg_num - 1].xcor() # Second to last segment (line 33 & 34)
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y) # Last segment move to second to last
        self.head.forward(MOVE_DISTANCE)

    def turn_snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

