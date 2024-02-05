from turtle import Turtle, Screen
import turtle
import pandas as pd

states = pd.read_csv('50_states.csv')

screen = Screen()
screen.title('U.S. States Game')


IMAGE = 'blank_states_img.gif'
screen.addshape(IMAGE)
turtle.shape(IMAGE)
screen.tracer(0)
turtle.penup()

i = 1
while True:
    answer_state = screen.textinput(title= f"Guess the State {i}/50", prompt="What's another stat's name? ")
    user_guess = answer_state.title()
    if user_guess in states['state'].values:
        x = int(states[states['state'] == answer_state.title()]['x'])
        y = int(states[states['state'] == answer_state.title()]['y'])
        print(x, y)
        turtle.goto(x, y)
        turtle.write(user_guess, align='left', font=('Arial', 5, 'normal'))
        turtle.goto(0, 0)
        screen.update()
        i += 1
    else:
        print('doesnt exists')

turtle.mainloop()