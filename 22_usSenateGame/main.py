import turtle 
import pandas as pd

#constatnts
SCREEN_TITLE = "U.S States Game"
IMAGE_FILE = "black_states_img.gif"
CSV_FILE = "50_states.csv"
OUTPUT_FILE = "states_to_learn.csv"

# function to initialize Turtle graphics
def initialize_turtle():
    screen = turtle.Screen()
    screen.title(SCREEN_TITLE)
    screen.addshape(IMAGE_FILE)
    turtle.shape(IMAGE_FILE)
    return screen

#function to read state from data from CSV
def read_state_data(file):
    try:
        data = pd.read_csv(file)
        return data
    except FileNotFoundError:
        print(f"Error: {file} not found")
        return None

#function to display a state on the map
def display_state(t, x, y, state_name):
    t.goto(x,y)
    t.write(state_name, align="center", font=("Arial", 12, "normal"))

def main():
    #Initialize turtle graphics
    screen = initialize_turtle()

    #read state data from csv
    state_data = read_state_data(CSV_FILE)
    if state_data is None:
        return
    
    all_states = state_data.state.to_list()
    guessed_states = []

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    while len(guessed_states) < 50:
        answer_state = screen.textinput(
            title = f"{len(guessed_states)}/ States Correct",
            prompt="what's another states name?"
        ).title()

        if answer_state == "Exit":
            missing_states = [state for state in all_states if state not in guessed_states]
            new_data = pd.DataFrame(missing_states, columns=["State"])
            new_data.to_csv(OUTPUT_FILE, index=False)
            break

        if answer_state in all_states and answer_state not in guessed_states:
            guessed_states.appened(answer_state)
            state_info = state_data[state_data.state == answer_state]
            display_state(t, int(state_info.x), int(state_info.y), answer_state)

    turtle.mainloop()

if __name__ == "__main__":
    main()