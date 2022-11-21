from turtle import Turtle
import random

class Food(Turtle):
    score = 1
    high_score = 0
    s = Turtle()

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


    def scoreboard(self):
        # self.s.hideturtle()
        # self.s.ht()
        self.s.reset()
        self.s.hideturtle()

        self.s.penup()
        self.s.goto(0, 250)
        self.s.color("yellow")
        self.s.write(f"Score = {self.score} and the high score is: {self.high_score}", False, align="center", font=('Sherif', 18, 'normal'))
        self.score += 1



    def resetScore(self):
        self.score = 0

    def game_over(self):
        self.goto(0, 0, )
        self.write("GAME OVER", align="center", font=('Sherif', 18, 'normal'))
        self.resetScore()


