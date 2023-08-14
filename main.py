import turtle
import pandas as pd


us_data = pd.read_csv('50_states.csv')
states_series = us_data['state']


turtle_pointer = turtle.Turtle()
turtle_pointer.penup()
turtle_pointer.hideturtle()


screen = turtle.Screen()
screen.title('States of the US Quiz!')
screen.bgpic('blank_states_img.gif')


score = 0
for _ in range(50):
    user_input = turtle.textinput("Your Answer", "Give me the 50 States in USA?").title()
    for index, row in us_data.iterrows():
        if user_input == row['state']:
            x, y = row['x'], row['y']
            turtle_pointer.goto(x, y)
            turtle_pointer.write(user_input)
     

screen.exitonclick()

