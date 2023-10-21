"""
 This program is has an example of a built in function that converts feet walked into
 a number of steps and returns such steps. The main program will take input from the 
 user in feet walked and then print the number of steps walked.

Date: 10/05/23
Author: Kevin Gallardo
Program Name: gallardo_kevin_steps.py

"""

# function definition 
def feet_to_steps(feet_walked):
   # do floor division to get num of steps walked
   steps_walked = feet_walked // 2.5

   return steps_walked


#print prompt and get user input
value = float(input("Please enter the distance travelled in feet: "))

# call to function that converts feet to steps
steps = feet_to_steps(value)

# print steps
print(f"{steps:.0f} steps")
