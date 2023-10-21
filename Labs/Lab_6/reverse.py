"""
 This program takes in a line of text as input, and outputs that line of text
 in reverse. The program repeats, ending only when the user enters "Quit",
 "quit", or "q" for the line of text.

Date: 09/28/23
Author: Keving Gallardo

"""

# take user input
user_input = input("Please Enter Your String: ")

# while loop checks to see if the ending word was put in as input
while (user_input != "Quit" and user_input != "quit" and user_input != "q"):
    # create empty list
    list = []

    # for loop in reversed
    for char in reversed(user_input):
        # add character to list
        list.append(char)

    # print characters in list
    for index in list:
        print(index, end="") 

    # print 2 spaces and ask user for another sentence or word
    print("\n")
    user_input = input("Please Enter Your String: ")
    
   
