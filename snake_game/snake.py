from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.all_turtle = []
        self.create_snake()
        self.head = self.all_turtle[0]
        

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake_segment(position)

    def add_snake_segment(self,position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.setpos(position)
        self.all_turtle.append(new_turtle)


    def extend_snake(self):
        self.add_snake_segment(self.all_turtle[-1].pos())

    # def sake_body(self):
    #     self.body = self.all_turtle[1:]
    #     for snake_body in self.body:
    #         if(self.head.distance(snake_body) < 10):
    #             new_main.game_is_on = False
    #             score_board.game_over()


    def move(self):
        for turtle_num in range(len(self.all_turtle)-1,0,-1):#(start,end,jumps)
            new_x_pos = self.all_turtle[turtle_num-1].xcor()
            new_y_pos = self.all_turtle[turtle_num-1].ycor()
            self.all_turtle[turtle_num].goto(new_x_pos,new_y_pos)
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
        

# t = Turtle()
# t.setheading(90)
# print(type(t.heading()))

# s = Snake()
# a=list(s.all_turtle[-1].pos())
# print(a)
# a[0]=a[0]-20
# print(a)


