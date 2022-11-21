from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)



snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# high_score = 0
with open("data.txt") as file:
    contents = file.read()
    high_score = int(contents)
    food.high_score = high_score
    file.close()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:

        if food.score > high_score:
            high_score = food.score
            food.high_score = high_score
            with open("data.txt", mode="w") as file:
                file.truncate(0)
                file.write(f"{high_score}")
                file.close()
        food.refresh()
        snake.extend()
        food.scoreboard()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        food.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            food.game_over()


        if segment == snake.head:
            pass

screen.exitonclick()