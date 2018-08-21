# run me if you want to play rock paper scissors

from rock_paper_scissors import start_game

while True:
    user_input = input("\n Press Enter to play, or press q then enter to quit ")
    if user_input.lower().strip("") == "q":
        quit()
    else:
        start_game()