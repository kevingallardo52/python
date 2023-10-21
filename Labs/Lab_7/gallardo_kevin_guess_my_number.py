"""
 This program is a game that generates a ramdom number between 1 and 100.
 The player will have ten attempts to guess the number. Each guess will have
 feed back and say if the guess is greater or smaller than the number. If the 
 player guesses correctly then the program will acknowledge succes and end. If
 the player runs out of attempts the program will let them know and it will end.

Date: 10/05/23
Author: Kevin Gallardo
Program Name: gallardo_kevin_guess_my_number.py

"""

# import to make random numbers
import random

# make random number between 1 - 100 inclusive
ran_num = random.randint(1,100)

#print(ran_num)

#print prompt
print("I have generated random number between 1 and 100. You will have 10 attempts to guess that number. ")

# for loop that itarates ten times
for i in range(10):
   # take guess as input and type cast to int
   guess = int(input(f"Guess {i+1}: "))

   # check to see if input is equal, greater than, or less than ran num
   if guess == ran_num:
      # if input is equal to ran num then print ack and break out of for loop
      print("You correctly guessed my random number!")
      break
   elif guess > ran_num:
      print("Your guess is greater than my random number. Try again.")
   else:
      print("Your guess is less than my random number. Try Again.")
