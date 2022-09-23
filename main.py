import turtle
from quiz_manager import QuizManager

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.setup(725, 491)
screen.addshape(image)
turtle.shape(image)

quiz_manager = QuizManager()

correct_guesses = []
keep_guessing = True
while keep_guessing:
    answer_state = screen.textinput(f"{len(correct_guesses)}/50 Guess the State",
                                    "What's another state's name?").title()

    if quiz_manager.add_state_on_map(answer_state):
        correct_guesses.append(answer_state)

    if len(correct_guesses) == 50:
        quiz_manager.announce_win()
        keep_guessing = False

screen.exitonclick()
