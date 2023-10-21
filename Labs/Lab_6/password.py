"""
 This program takes a simple password and makes it stronger by replacing
 characters useing the key below, and by appending "!" to the end of the
 input string.

•  o becomes 0
• i becomes 1
• a becomes @
• e becomes 3
• A becomes 4
• B becomes 8
• s becomes $

Date: 09/28/23
Author: Keving Gallardo

"""

# take user input
password = input("Please Enter Your Password: ")

# create list to add characters to it
list = []

# go through each characted and see if they are one of the special characters, if they are then add there corresponding substitute to the list
# if they are not a special character then just add that character to the list
for char in password:
     if char == "o":
          list.append("0")
     elif char == "i":
          list.append("1")
     elif char == "a":
          list.append("@")
     elif char == "e":
          list.append("3")
     elif char == "A":
          list.append("4")
     elif char == "B":
          list.append("8")
     elif char == "s":
          list.append("$")
     else:
          list.append(char)
# after going through all the characters in the string then append "!" to the end
else: 
     list.append("!")

# print every value in the string on the same line and at the end of the for loop print a space
for value in list:
     print(value, end="")
else:
     print()