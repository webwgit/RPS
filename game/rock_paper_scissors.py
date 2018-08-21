''' how to run:
    run the play_game script from the command prompt or termianl, eg: python script.py


Code by: Mohammed
written with Python 3.5
     '''


from random import randint


def computer_choice():
    rand_num = randint(1,3)
    if rand_num == 1:
        return "r"
    elif rand_num == 2:
        return "s"
    elif rand_num == 3:
        return 'p'

def who_wins(user, comp):
    if user == comp:
        return "It's a tie!"

    elif user == "r":
        if comp == "p":
            return "I win! Paper covers the Rock"
        else:
            return "You win, Rock destroyes Scissors"

    elif user == "p":
        if comp == "s":
            return "I win! Scissors cut Paper"
        else:
            return "You win, Paper covers Rock"

    elif user == "s":
        if comp == "r":
            return "I win! Rock break Scissors"
        else:
            return "You win, Scissors cut Paper"


def start_game():
    start_text = ''' \n Welcome to the mortal Rock Paper Scissors game, choose r for Rock, p for Paper, s for Scissors \n '''
    user_input = input(start_text)
    user_input = user_input.strip().lower() #to deal with the any white space or capital letters
    if user_input == "r" or user_input == "s" or user_input == "r":
       # print (" You chose "+ user_input)
        com = computer_choice()
        print (" I choose " + com)
        print(" "+who_wins(user_input, com))
    else:
        print(" \n Please choose proper input. Only a letter of r, p, s for Rock Paper or Scissors \n")

