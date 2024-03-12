import turtle
import random

screen = turtle.Screen()
screen.setup(500, 400)

colors = ['red', 'orange', 'green', 'blue', 'yellow', 'purple']

bet = screen.textinput("make your bet", "which turtle will win the race? enter color: ")
correct = True
while correct:
    bet = screen.textinput("make your bet", "which turtle will win the race? enter color: ")
    if bet in colors:

        user_bet = (bet, bet)
        coordinates = [-100, -60, -20, 20, 60, 100]

        is_race_on = False
        if user_bet:
            is_race_on = True

        turtles = []

        for i in range(6):
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.shape("turtle")
            new_turtle.color(colors[i])
            new_turtle.goto(-235, coordinates[i])
            turtles.append(new_turtle)

        while is_race_on:
            for j in turtles:
                if j.xcor() > 230:
                    if j.color() == user_bet:
                        print(f"You win. The {bet} turtle is the winner.")
                    else:
                        print(f"You lose. The {j.color()[0]} turtle is the winner.")
                    is_race_on = False
                    correct = False
                    break
                random_distance = random.randint(0, 10)
                j.forward(random_distance)
    else:
        print("Please enter a valid color!")

screen.exitonclick()
