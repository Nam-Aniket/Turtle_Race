from turtle import *
from random import *

turtle_s = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
all_turtle = []
is_game_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_inp = screen.textinput("Make your Bet", "Which Turtle will win? Enter your color: ").lower()
y_index = -150
x_index = -230
for turtle_index in turtle_s:
    turtle1 = Turtle(shape="turtle")
    turtle1.penup()
    turtle1.color(turtle_index)
    turtle1.goto(x_index, y_index)
    y_index += 50
    all_turtle.append(turtle1)

# Condition
if user_inp:
    is_game_on = True

while is_game_on:
    for turtle in all_turtle:
        turtle.forward(randint(0, 15))
        x_cor = turtle.xcor()
        if x_cor > 230:
            if turtle.pencolor() == user_inp:
                print(f"You guessed correctly, {turtle.pencolor()} Turtle wins")
            else:
                print(f"Good lick next time, You lose. {turtle.pencolor()} won!")

            is_game_on = False

screen.exitonclick()
