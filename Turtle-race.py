import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(500, 400)

# List of available colors for turtles
colors = ['red', 'orange', 'green', 'blue', 'yellow', 'purple']

# Ask the user to make a bet on the winning turtle
bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter color: ")

# Ensure that the user's bet is a valid color
correct = True
while correct:
    bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter color: ")
    if bet in colors:
        # If the bet is valid, set the user's bet
        user_bet = (bet, bet)
        coordinates = [-100, -60, -20, 20, 60, 100]

        is_race_on = False
        if user_bet:
            is_race_on = True

        turtles = []

        # Create turtles with different colors and initial positions
        for i in range(6):
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.shape("turtle")
            new_turtle.color(colors[i])
            new_turtle.goto(-235, coordinates[i])
            turtles.append(new_turtle)

        # Start the race
        while is_race_on:
            for j in turtles:
                # Check if any turtle has reached the finish line
                if j.xcor() > 230:
                    # Check if the winning turtle matches the user's bet
                    if j.color() == user_bet:
                        print(f"You win. The {bet} turtle is the winner.")
                    else:
                        print(f"You lose. The {j.color()[0]} turtle is the winner.")
                    is_race_on = False
                    correct = False
                    break
                # Move each turtle forward by a random distance
                random_distance = random.randint(0, 10)
                j.forward(random_distance)
    else:
        # Prompt the user to enter a valid color if the input is invalid
        print("Please enter a valid color!")

# Close the screen when clicked
screen.exitonclick()
