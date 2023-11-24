from turtle import Turtle, Screen

starting_positions = [(0,0), (-20,0), (-40,0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position=position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x,y=new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        # add new segment to game
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(10000,10000)
        self.segments.clear()
        self.create_snake()
        self.head =  self.segments[0]
    