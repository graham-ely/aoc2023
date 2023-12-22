from functools import cmp_to_key
from math import lcm

# 34:21 from my start of 19
#data = open("19_test_data.txt", "r")
data = open("19_data.txt", "r")

def find_next_coord (coord, prev_coord, char) -> list:
    new_coord = coord.copy()
    if(char == '|'):
        if( prev_coord[0] == coord[0] - 1 ):
            new_coord[0] += 1
        else:
            new_coord[0] -= 1
    if(char == '-'):
        if( prev_coord[1] == coord[1] - 1 ):
            new_coord[1] += 1
        else:
            new_coord[1] -= 1
    if(char == 'L'):
        if( prev_coord[0] == coord[0] ):
            new_coord[0] -= 1
        else:
            new_coord[1] += 1
    if(char == 'F'):
        if( prev_coord[0] == coord[0] ):
            new_coord[0] += 1
        else:
            new_coord[1] += 1
    if(char == 'J'):
        if( prev_coord[0] == coord[0] ):
            new_coord[0] -= 1
        else:
            new_coord[1] -= 1
    if(char == '7'):
        if( prev_coord[0] == coord[0] ):
            new_coord[0] += 1
        else:
            new_coord[1] -= 1
    return new_coord

#vars outside loop
map = []
animal_start = [0,0]

for i_idx, line in enumerate(data):
    #iteration through lines
    if( 'S' in line ):
        animal_start = [i_idx, line.index('S')]
    #remove newline characters
    items = line.split()
    map.append(*items)
    #print(sum)

# we start with sum at 1 going down immediately, which works for both mazes
sum           = 1
current_char  = '|'
prev_coord    = animal_start
current_coord = [prev_coord[0] + 1, prev_coord[1]]
new_coord     = [0,0]

while( current_char != 'S' ):
    #print("Prev:", prev_coord)
    #print("Current:", current_coord, current_char)
    new_coord = find_next_coord(current_coord, prev_coord, current_char)
    prev_coord = current_coord
    current_coord = new_coord
    current_char = map[current_coord[0]][current_coord[1]]
    sum += 1
    
print(sum)
print(sum / 2)