''' You can run this test from cmd or terminal like this: python -m pytest, note that this is a recurssive call '''

import pytest
import rock_paper_scissors

def test_who_wins():
    val = rock_paper_scissors.who_wins("r","r")
    assert val == "It's a tie!"

    val = rock_paper_scissors.who_wins("p","p")
    assert val == "It's a tie!"

    val = rock_paper_scissors.who_wins("s","s")
    assert val == "It's a tie!"

    val = rock_paper_scissors.who_wins("r","p")
    assert val == "I win! Paper covers the Rock"

    val = rock_paper_scissors.who_wins("r","s")
    assert val == "You win, Rock destroyes Scissors"

    val = rock_paper_scissors.who_wins("p","r")
    assert val == "You win, Paper covers Rock"

    val = rock_paper_scissors.who_wins("p","s")
    assert val == "I win! Scissors cut Paper"

    val = rock_paper_scissors.who_wins("s","p")
    assert val == "You win, Scissors cut Paper"

    val = rock_paper_scissors.who_wins("s","r")
    assert val == "I win! Rock break Scissors"


