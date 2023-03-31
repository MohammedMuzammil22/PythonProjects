from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake_segment(position)

    def add_snake_segment(self,position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.setpos(position)
        self.snake_segments.append(new_turtle)


    def extend_snake(self):
        self.add_snake_segment(self.snake_segments[-1].pos())


    def move(self):
        for turtle_num in range(len(self.snake_segments)-1,0,-1):#(start,end,jumps)
            new_x_pos = self.snake_segments[turtle_num-1].xcor()
            new_y_pos = self.snake_segments[turtle_num-1].ycor()
            self.snake_segments[turtle_num].goto(new_x_pos,new_y_pos)
        self.head.forward(20)

    def up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)
        
    def down(self):
        if(self.head.heading() != UP):
            self.head.setheading(DOWN)
        
    def left(self):
        if(self.head.heading() != RIGHT):
            self.head.setheading(LEFT)
        
    def right(self):
        if(self.head.heading() != LEFT):
            self.head.setheading(RIGHT)
        
    def reset(self):
        for seg in self.snake_segments:
            seg.goto(1000,1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]
