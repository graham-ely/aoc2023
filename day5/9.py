# 40:21 from my start of 7
#data = open("9_test_data.txt", "r")
data = open("9_data.txt", "r")
steps = ['seed-to-soil',
'soil-to-fertilizer',
'fertilizer-to-water',
'water-to-light',
'light-to-temperature',
'temperature-to-humidity',
'humidity-to-location']
#vars outside loop
seeds = []
step_num = 0
instructions = []

#extract data
for idx, line in enumerate(data):
    #iteration through lines
    split_line = line.split()
    if(idx == 0):
        seeds = split_line
        seeds.pop(0)
    elif( len(split_line) > 0 and split_line[0] in steps):
        line_title = split_line[0]
        step_num = steps.index(line_title)
    elif( line[0] != 's' and len(line) > 1):
        add_arr = []
        add_arr.append(int(step_num))
        for item in split_line:
            add_arr.append(int(item))
        instructions.append(add_arr)
    #iterate vars oustside loop
    #clear flags

seed_locations = []

for seed in range(1333399202,1621024032,1):
    current_seed_val = int(seed)
    print(seed)
    step = 0
    #for step in range(7):
    for inst in instructions:
        if( inst[0] > step ):
            step += 1
        if( inst[0] == step ):
            if( current_seed_val >= inst[2] and current_seed_val <= ( inst[2] + inst[3] )):
                #seed in range, find new value and increment step
                current_seed_val = inst[1] + (current_seed_val - inst[2])
                step += 1
    seed_locations.append(current_seed_val)

print(seed_locations)
print(min(seed_locations))