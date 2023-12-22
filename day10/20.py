from functools import cmp_to_key
from math import lcm

# 98:08:55 from my start of 19 lol (I started it, worked for about an hour, and then left for dinner and didn't pick it up for days. probably about 2 hours on this problem)
# I'd discussed with a friend beforehand so I had some inkling of the trick for this one but still spent awhile dealing with the corners
# I also cleaned this up a bit after since it was pretty ugly with copy/pastes instead of functions
#data = open("20_test_data_2.txt", "r")
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
    if( 'S' in line ):
        animal_start = [i_idx, line.index('S')]
    items = line.split()
    map.append(*items)

# we start with sum at 1 going down immediately, which works for both mazes
sum           = 1
current_char  = '|'
prev_coord    = animal_start
current_coord = [prev_coord[0] + 1, prev_coord[1]]
new_coord     = [0,0]
loop          = []
loop.append(prev_coord)
loop.append(current_coord)

#establish loop
while( current_char != 'S' ):
    new_coord = find_next_coord(current_coord, prev_coord, current_char)
    prev_coord = current_coord
    current_coord = new_coord
    current_char = map[current_coord[0]][current_coord[1]]
    loop.append(current_coord)
    sum += 1

def handle_pipe(last_corner, current_char) -> int:
    if( current_char == '-' or current_char == '|' ):
        return 0
    elif( last_corner == 'F' or last_corner == 'J' ):
        if( current_char == 'J' or current_char == 'F' ):
            return 1
        elif( current_char == '7' or current_char == 'L' ):
            return -1
    elif( last_corner == '7' or last_corner == 'L' ):
        if( current_char == 'L' or current_char == '7' ):
            return 1
        elif( current_char == 'F' or current_char == 'J' ):
            return -1

def process_point(x_coord, y_coord):
    global pipe_count
    global last_corner
    current_char = map[x_coord][y_coord]

    if( last_corner == '' and ( current_char == '-' or current_char == '|' )):
        pipe_count += 1
    elif( current_char in ['F','J','7','L'] ):
        if( last_corner == '' ):
            last_corner = current_char
        else:
            handled_pipe = handle_pipe(last_corner, current_char)
            if handled_pipe == 1:
                last_corner = ''
                pipe_count += 1
            elif handled_pipe == -1:
                last_corner = ''

inside_count = 0
last_corner  = ''
global pipe_count

for o_idx, line in enumerate(map):
    last_corner  = ''
    for i_idx, point in enumerate(line):
        last_corner  = ''
        if ( [o_idx, i_idx] in loop ):
            continue
        else:
            pipe_count = 0
            for x in range(o_idx):
                if ( [x, i_idx] in loop ):
                    process_point(x, i_idx)
            if( pipe_count % 2 != 0 ):
                pipe_count = 0
                last_corner  = ''
                for x in range(len(map) - o_idx):
                    if ( [len(map) - x, i_idx] in loop ):
                        process_point(len(map) - x, i_idx)
                if( pipe_count % 2 != 0 ):
                    pipe_count = 0
                    last_corner  = ''
                    for x in range(len(map[0]) - i_idx):
                        if ( [o_idx, len(map[0]) - x] in loop ):
                            process_point(o_idx, len(map[0]) - x)
                    if( pipe_count % 2 != 0 ):
                        pipe_count = 0
                        last_corner  = ''
                        for x in range(i_idx):
                            if ( [o_idx, x] in loop ):
                                process_point(o_idx, x)
                        if( pipe_count % 2 != 0 ):
                            inside_count += 1
                            print([o_idx, i_idx])
    
print(inside_count)