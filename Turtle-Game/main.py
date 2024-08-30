import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()

    # Detect collision with cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            print(f"You have cleared {scoreboard.level - 1} levels")

    # Detect the winning spot
    if player.reached_destination():
        scoreboard.change_level()
        player.re_start()
        car_manager.level_up()

screen.exitonclick()
