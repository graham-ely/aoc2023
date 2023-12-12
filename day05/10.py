# hours from my start of 9, this one was a bit of a bear
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
        add_arr.append(int(split_line[0]))
        add_arr.append(int(split_line[1]))
        add_arr.append(int(split_line[2]))
        add_arr.append(int(split_line[1]) + int(split_line[2]) - 1)
        instructions.append(add_arr)
        #iterate vars oustside loop
        #clear flags

seed_locations = []
real_seeds     = []
first_seed     = 0
loop_min       = 50855030#44300000 #157211394
loop_max       = 50855038#229536766#2692583476
loop_step      = 1#17#33
#300627200 by 100
solution_flag = False
solution_loc = 10000000000000000
solution_seed = 0

while (solution_flag is False and loop_min < loop_max):
    current_step_min = loop_min 
    step = 6
    for inst in reversed(instructions):
        if( inst[0] < step ):
            step -=1
        if( inst[0] == step ):
            if( inst[1]  <= current_step_min and ( inst[1] + inst[3] - 1 ) >= current_step_min ):
                current_step_min = current_step_min + ( inst[2] - inst[1] )
                step-=1

    for idx, seed in enumerate(seeds):
        if(idx % 2 == 0):
            first_seed = int(seed)
        else:
            if( current_step_min >= first_seed and current_step_min <= ( first_seed + int(seed) - 1 ) ):
                if( loop_min < solution_loc ):
                    solution_flag = True
                    solution_seed = current_step_min
                    solution_loc  = loop_min
    
    print("lmin", loop_min)
    loop_min += loop_step



print("Location number: ", solution_loc, " from seed number: ", solution_seed)

 #sanity check result
seeds = []
seeds.append(2692583476)
# manual testing -- solved off by one issue here
seeds.append(1400877516)
seeds.append(1400877517)
seeds.append(1400877518)
seeds.append(solution_seed)
for seed in seeds:
    current_seed_val = int(seed)
    step = 0
    for inst in instructions:
        if( inst[0] > step ):
            step += 1
        if( inst[0] == step ):
            if( current_seed_val >= inst[2] and current_seed_val <= inst[4] ):
                #seed in range, find new value and increment step
                current_seed_val = inst[1] + (current_seed_val - inst[2])
                step += 1
    seed_locations.append(current_seed_val)

print(seeds)
print(seed_locations)
#print(min(seed_locations))