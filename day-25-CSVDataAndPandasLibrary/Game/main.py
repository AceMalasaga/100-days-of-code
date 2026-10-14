import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

#Create a separate turtle for write
write = turtle.Turtle()
write.hideturtle()
write.penup()

score = 0

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while score < len(all_states):
    user_guess = screen.textinput(title=f"{score}/50 State Correct", prompt="What's another state's name?").title()

    if user_guess in all_states and user_guess not in guessed_states:
        print("You guessed the correct state")
        #Get the correct answer coordinates
        state_data = data[data.state == user_guess]
        #Convert the coordinates to int since most of the time it get float or int64
        #Use item() to get the value not the series of objects
        x_cor = int(state_data.x.item())
        y_cor = int(state_data.y.item())
        write.goto(x_cor, y_cor)
        write.write(user_guess)
        score += 1
        guessed_states.append(user_guess)

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()