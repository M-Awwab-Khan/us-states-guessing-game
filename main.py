from turtle import Screen
import turtle
import pandas as pd

states = pd.read_csv('50_states.csv')

screen = Screen()
screen.title('U.S. States Game')


IMAGE = 'blank_states_img.gif'
screen.addshape(IMAGE)
turtle.shape(IMAGE)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
guessed_states = []
i = 1   
while i <= 50:
    answer_state = screen.textinput(title= f"Guess the State {i}/50", prompt="What's another stat's name? ")
    if answer_state != None:
        user_guess = answer_state.title()

        if user_guess in states['state'].values:
            guessed_states.append(user_guess)
            x = states[states['state'] == user_guess].x.item()
            y = states[states['state'] == user_guess].y.item()
            writer.goto(x, y)
            writer.write(user_guess, align='left', font=('Arial', 7, 'normal'))
            i += 1
    else:
        left_states = list(set(states['state']).difference(set(guessed_states)))
        left_states.sort()
        pd.DataFrame({'states': left_states}).to_csv('states_to_learn.csv')
        break
