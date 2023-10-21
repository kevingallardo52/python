"""
 This program is an example of a 2x2 matrix that at fist all entries will be initialized to 0,
 except the position of where the random walker begins, then it will calcute a random number
 between 1-20 and from that number it will decide where to move the walker. The only options are
 Up Down Left Right. And the movement will be taking place in the grid, so there has to be checks 
 to be sure that the random walker does not go out of bounds. Every time the random walker moves 
 to a new spot the location on the matrix will be updated to reflect how many times the random walker
 has visited such spot. In the end it prints the heat matrix, the ending positon for the walker, and
 the manhattan distance from where the walker ended to where it began. 

Date: 10/19/23
Author: Kevin Gallardo
Program Name: gallardo_kevin_random_walk.py

"""
import random
import helper

def manhattan_distance(start, end):
    distance = abs((start[0] - end[0])) + abs((start[1] - end[1]))
    return distance

row = 15
colum = 15
num_moves = 100

# makes matrix or nested list
heat_matrix = [0] * row
for x in range (row):
    heat_matrix[x] = [0] * colum

# finds middle of row and colum
mid_row = (len(heat_matrix)//2 )
mid_colum = (len(heat_matrix[0])//2)

# variables to keep track of positions
start_position = [mid_row, mid_colum]
current_position = [mid_row, mid_colum]

# init position
heat_matrix[start_position[0]][start_position[1]] = 1

# print 
print("Starting Grid")
helper.print_matrix(heat_matrix)

random.seed(43543)

for i in range(num_moves):

    num = random.randint(1,20)

    # move up modifies row
    if 1 <= num <= 7 and current_position[0] > 0:
        current_position[0] -= 1
    
    # moves down modifies row
    elif 8 <= num <= 14 and current_position[0] < row - 1:
        current_position[0] += 1

    # moves left modifies colum
    elif 15 <= num <= 17 and current_position[1] > 0:
        current_position[1] -= 1

    # moves right modifies colum
    elif 18 <= num <= 20 and current_position[1] < colum - 1:
        current_position[1] += 1
    
    # if any of the previous moves did not execute then it means
    # you were at one of the edges. Sine you cannot move it will decrement the iterator "i"
    # and jump to the next iteration and try a different random number and see if it can move
    else:
        i -= 1
        continue

    # valid move so update the heat matrix
    heat_matrix[current_position[0]][current_position[1]] += 1


print()
print("Movement Heat Map")
helper.print_matrix(heat_matrix)

print()
print(f"Agent's Final Position: ({current_position[0]},{current_position[1]})")
print(f"Distance From Start: {manhattan_distance(start_position, current_position)}")