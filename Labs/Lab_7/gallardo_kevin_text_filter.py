"""
 This program will have one user defined funtion. One will take a string as
 an argument which will represent a message to be sent and return the message without 
 these banned words: Turkey, Dog, Fox, Cat, Chicken. The main program will take in input
 from the user and call the user defined function to remove the banned words from the message
 and then it will print the new message without the banned words.

Date: 10/05/23
Author: Kevin Gallardo
Program Name: gallardo_kevin_filter.py

"""

# function definition 
# define banned word list once and use inside function
banned_words = ["Turkey","Dog", "Fox", "Cat", "Chicken"]
def text_filter(message):
   # split string into lists
   list = message.split()

   # check if each word in list to see if it is in the list of banned words, if it is then remove word from list
   # [:] makes a copy of the list to use in the for loop
   for word_in_list in list[:]:
      for banned_word in banned_words:
         if banned_word == word_in_list:
            list.remove(banned_word)

   # join list element into a string and for element add a space in between
   new = ' '.join(list)

   # return edited string
   return new


# print prompt and get user input
message = input(": ")

# save edited string into new variable
new_message = text_filter(message)

# print input and output
print(f"Input Message: {message}")
print(f"Output Message: {new_message}")
