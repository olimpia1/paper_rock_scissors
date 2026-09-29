# unfair computer
# part one
# from enum import Enum
#
# user_choice = input()
#
# class ComputerChoice(Enum):
#     rock = "rock"
#     paper = "paper"
#     scissors = "scissors"
#
#
# computer_choice = ['rock', 'paper', 'scissors']
#
# if user_choice == "rock":
#     print(f"Sorry, but the computer chose {ComputerChoice.paper.value}")
# elif user_choice == "paper":
#     print(f"Sorry, but the computer chose {ComputerChoice.scissors.value}")
# else:
#     print(f"Sorry, but the computer chose {ComputerChoice.rock.value}")

# Equalizing chances
# part two

# import random
#
# computer_choice = random.choice(["rock", "paper", "scissors"])
# user_choice = input()
# if user_choice == computer_choice:
#     print(f"There is a draw ({computer_choice})")
# elif (user_choice == "rock" and computer_choice == "paper" or
#       user_choice == "paper" and computer_choice == "scissors" or
#       user_choice == "scissors" and computer_choice == "rock"):
#     print(f"Sorry, but the computer chose {computer_choice}")
# else:
#     print(f"Well done. The computer chose {computer_choice} and failed")

# Endless game
# part three

# import random
#
# possible_user_choices = ["rock", "paper", "scissors", "!exit"]
#
# while True:
#     computer_choice = random.choice(["rock", "paper", "scissors"])
#     user_choice = input()
#     while user_choice not in possible_user_choices:
#         print("Invalid input")
#         user_choice = input()
#     if user_choice == computer_choice:
#         print(f"There is a draw ({computer_choice})")
#     elif (user_choice == "rock" and computer_choice == "paper" or
#           user_choice == "paper" and computer_choice == "scissors" or
#           user_choice == "scissors" and computer_choice == "rock"):
#         print(f"Sorry, but the computer chose {computer_choice}")
#     elif user_choice == "!exit":
#         print("Bye!")
#         break
#     else:
#         print(f"Well done. The computer chose {computer_choice} and failed")

# Scoring the game
# part four

# import random
#
# possible_user_choices = ["rock", "paper", "scissors", "!exit", "!rating"]
#
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}")
#
# with open("rating.txt", "r") as rating_file:
#     names_and_ratings = [line.strip() for line in rating_file.readlines()]
#     names_ratings = {el.split()[0]: int(el.split()[1]) for el in names_and_ratings}
#
# if user_name in names_ratings:
#     rating = names_ratings[user_name]
# else:
#     rating = 0
#     names_ratings.update({user_name: rating})
#
# while True:
#     computer_choice = random.choice(["rock", "paper", "scissors"])
#     user_choice = input()
#     while user_choice not in possible_user_choices:
#         print("Invalid input")
#         user_choice = input()
#     if user_choice == computer_choice:
#         print(f"There is a draw ({computer_choice})")
#         rating += 50
#     elif (user_choice == "rock" and computer_choice == "paper" or
#           user_choice == "paper" and computer_choice == "scissors" or
#           user_choice == "scissors" and computer_choice == "rock"):
#         print(f"Sorry, but the computer chose {computer_choice}")
#     elif user_choice == "!exit":
#         print("Bye!")
#         break
#     elif user_choice == "!rating":
#         print(f"Your rating: {rating}")
#     else:
#         print(f"Well done. The computer chose {computer_choice} and failed")
#         rating += 100

# More options
# part five

import random
from collections import deque

user_name = input("Enter your name: ")
print(f"Hello, {user_name}")

user_list_of_the_options = input()
default_options = ["rock", "paper", "scissors"]

if len(user_list_of_the_options) == 0:
    user_list_of_the_options = default_options
    computer_options = default_options
else:
    user_list_of_the_options = user_list_of_the_options.split(",")
    computer_options = user_list_of_the_options

print("Okay, let's start")


def find_beat_and_defeated(collection_of_options, option):
    collection_of_options = deque(collection_of_options)
    middle = len(collection_of_options) // 2
    current = collection_of_options.index(option)

    collection_of_options.rotate(middle - current)
    collection_of_options = list(collection_of_options)
    beat = collection_of_options[0:middle]
    is_defeated = collection_of_options[middle + 1:]
    return beat, is_defeated


possible_user_choices = user_list_of_the_options + ["!exit", "!rating"]

with open("rating.txt", "r") as rating_file:
    names_and_ratings = [line.strip() for line in rating_file.readlines()]
    names_ratings = {el.split()[0]: int(el.split()[1]) for el in names_and_ratings}

if user_name in names_ratings:
    rating = names_ratings[user_name]
else:
    rating = 0
    names_ratings.update({user_name: rating})

while True:
    computer_choice = random.choice(computer_options)
    user_choice = input()
    while user_choice not in possible_user_choices:
        print("Invalid input")
        user_choice = input()
    if user_choice == "!rating":
        print(f"Your rating: {rating}")
    elif user_choice == "!exit":
        print("Bye!")
        break

    elif user_choice == computer_choice:
        print(f"There is a draw ({computer_choice})")
        rating += 50
    else:
        beat_it, are_defeated = find_beat_and_defeated(computer_options, user_choice)
        if computer_choice in are_defeated:
            print(f"Sorry, but the computer chose {computer_choice}")
        else:
            print(f"Well done. The computer chose {computer_choice} and failed")
            rating += 100
