from turtle import Turtle
import pandas as pd

FONT = ("Courier", 13, "normal")
WINNER_FONT = ("Cambria", 30, "normal")

states_df = pd.read_csv("50_states.csv")

states_list = []
for index in range(0, len(states_df.index)):
    row = states_df.iloc[index].to_dict()
    states_list.append(row)

states_dict = {}
for state_data in states_list:
    states_dict[state_data["state"]] = (state_data["x"], state_data["y"])


class QuizManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.up()
        self.hideturtle()
        self.states = states_dict

    def add_state_on_map(self, user_answer):
        if user_answer in self.states:
            self.goto(self.states[user_answer])
            self.write(user_answer, False, "center", FONT)
            return True
        else:
            return False

    def announce_win(self):
        self.goto(0, 0)
        self.write("🎉 YOU WON! 🎉", False, "center", WINNER_FONT)
