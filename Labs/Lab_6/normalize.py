"""
 This program takes as input the number of values that will be given,
 then it will take the values. After that it will normalize the values
 by dividing it by the lastest of the given values and then print the 
 normalized values.

Date: 09/28/23
Author: Keving Gallardo

"""

# take user input
numValues = int(input("Please enter the number of floating-point values: "))

# make empty list
list = []

# check to see if the values will be bigger than two
if(numValues >= 2):
    # take input for values dynamically and fill list
    for i in range(numValues):
        list.append(float(input("Please enter a floating-point value: ")))




    # get max value
    max = 0
    for value in list:
        if (value > max):
            max = value

    # do for loop and print the normalized values
    print("\nNormalized Floating-Point Values:")
    for value in list:
        ans = value / max 
        print(f"{ans:.2f}")

# if the values entered are 1
elif(numValues == 1):
    num = float(input("Please enter a floating-point value: "))
    print("\nNormalized Floating-Point Values:")
    print(f"{num/num:.2f}")
else:
    # if the values entered are 0 or negative
    print("\nThanks for trying")

