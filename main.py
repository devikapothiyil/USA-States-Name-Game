import turtle
import pandas

screen=turtle.Screen()
screen.title("US States Name Game")

img="blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data=pandas.read_csv("50_states.csv")
all_states= data.state.to_list()
guesses_states=[]

while len(guesses_states) < 50:
    answer_state = screen.textinput(title=f"{len(guesses_states)}/50 States Correct",
                                    prompt="Guess another state's name").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guesses_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]  # row of data
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

missing_states=[]
for states in all_states:
    if states not in guesses_states:
        missing_states.append(states)

missed_state_dict={
    "Missed States":missing_states
}

df=pandas.DataFrame(missed_state_dict)
df.to_csv("missed_states.csv")
