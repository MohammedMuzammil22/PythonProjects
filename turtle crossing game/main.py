import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.onkey(fun=player.go_up,key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.generate_car()
    car_manager.move_cars()
    scoreboard.display_level()
    screen.update()

    # detecting turtle hit by car
    for c in car_manager.all_cars:
        if(player.distance(c)<23.5):#20
            scoreboard.game_over()
            game_is_on = False

    # detecting turtle successfully crossed
    if(player.ycor()>280):
        player.reset_player_position()
        scoreboard.update_level()
        car_manager.increase_car_speed()
        


screen.exitonclick()