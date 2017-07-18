# This is the poroperty of Ryan Odum with a MIT License
"""This program make a hangman game.
It gives you 10 tries to guess
the secret word."""

import random
import os

list = ["computer", "laptop", "keyboard", "mouse", "network", "desktop", "windows", "linux", "flashdrive"]

secret_word = random.choice(list)

# static variables
previous = []
tries = 0
wrong = []

os.system("say Welcome to my hangman game")
os.system("say The objective is to guess the secret word within your ten tries.")
print "Welcome to my hangman game"
print "The objective is to guess the secret word within your ten tries."
# check for valid entry
def get_guess():
    while True:
        global tries
	print2()
        guess = raw_input("Guess: ").lower()
	os.system("say you guessed: " + guess)
        print "You guess: " + guess
        if guess not in secret_word:
            os.system("say " + str(10 - tries) + " incorrect guesses left.")
            print str(10 - tries) + " incorrect guesses left. "
            if guess in wrong:
                os.system("say You have already guess " + guess)
                print "You have already guess " + guess
            elif tries < 10 and guess not in wrong:
                tries = tries + 1
                wrong.append(guess)
                print "Your wrong guesses: " + str(wrong)
        if tries >= 10:
	    os.system("say Gameover!")
            print "Gameover!"
            os.system("say The secret word was " + secret_word + ".")
            print "The secret word was " + secret_word + "."
	    quit()
        if guess in secret_word:
	    os.system("say " +  guess + " is in the secret word")
            print guess + " is in the secret word"
            previous.append(guess)
        if len(guess) != 1:
	    os.system("say Your guess must have exactly one character!")
            print "Your guess must have exactly one character!"
        elif not guess.isalpha():
	    os.system("say Guess must be a lowercase letter!")
            print "Guess must be a lowercase letter!"

# update and solve word
def print2():
    word = ""


    for lt in secret_word:
        if lt in previous:
            word += lt
        else:
            word += "-"

    print word

    if word == secret_word:
	os.system("say You win")
        print "You win"
	quit()
        return False


get_guess()
