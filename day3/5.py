# 40:30 from my start of 5
#data = open("5_test_data.txt", "r")
data = open("5_data.txt", "r")

def is_adjacent(start, end) -> bool:
    adjacent = False

    for symbol in symbol_coordinates:
        if symbol[0] >= start[0] - 1 and symbol[0] <= start[0] + 1:
            if symbol[1] >= start[1] - 1 and symbol[1] <= end[1] + 1:
                adjacent = True
        
    return adjacent

#vars outside loop
sum = 0
symbols = [ '*', '%', '@', '$', '&', '#', '/', '=', '+', '-', '^', '!']
symbol_coordinates = []
numbers = []

for o_idx, line in enumerate(data):
    #iteration through lines
    number_in_prog = False
    number = '0'
    number_start = (0,0)

    for idx, item in enumerate(line):
        #iteration through line if needed
        if item.isdigit():
            if(number_in_prog == False):
                number_start = [o_idx, idx]
                number_in_prog = True
            number += str(item)
        elif item in symbols:
            number_in_prog = False
            symbol_coordinates.append([o_idx, idx])
        else:
            number_in_prog = False
        
        if ( number_in_prog == False and int(number) > 0 ) or ( number_in_prog == True and idx == len(line) - 1 ):
            numbers.append([number, number_start, [o_idx, idx - 1]])
            number = '0'
            number_start = (0,0)

    #iterate vars oustside loop
    #clear flags
for number3 in numbers:
    if is_adjacent(number3[1], number3[2]):
        sum += int(number3[0])
        #print(number3)

#print( symbol_coordinates )
#print( numbers )
print(sum)