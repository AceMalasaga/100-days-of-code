import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Correct", prompt="What's another state's name?")

    answer_state = answer_state.title()

    if answer_state == "Exit":
        # not_guessed_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         not_guessed_states.append(state)

        #Practice of list comprehension
        not_guessed_states = [state for state in all_states if state not in guessed_states]
        data = pd.DataFrame(not_guessed_states)
        data.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_info = data[data.state == answer_state]
        x_coordinate = state_info.x.item()
        y_coordinate = state_info.y.item()
        t.goto(x_coordinate, y_coordinate)
        t.write(answer_state)
        guessed_states.append(answer_state)