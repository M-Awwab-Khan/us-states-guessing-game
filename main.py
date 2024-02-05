from turtle import Turtle, Screen
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

i = 1
while i <= 50:
    answer_state = screen.textinput(title= f"Guess the State {i}/50", prompt="What's another stat's name? ")
    user_guess = answer_state.title()
    if user_guess in states['state'].values:
        x = states[states['state'] == user_guess].x.item()
        y = states[states['state'] == user_guess].y.item()
        writer.goto(x, y)
        writer.write(user_guess, align='left', font=('Arial', 7, 'normal'))
        i += 1
    else:
        print('doesnt exists')
