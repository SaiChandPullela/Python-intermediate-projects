from turtle import Turtle
FONT = ("Courier", 24, "normal")
game_over_position = (-100, 0)

class Scoreboard(Turtle):

    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.update_level()

    def update_level(self):
        self.write(f"Level {self.level}", font=FONT)

    def change_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(game_over_position)
        self.write("GAME OVER ", font=FONT)

