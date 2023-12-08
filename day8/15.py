from functools import cmp_to_key

# 39:11 from my start of 15
#data = open("15_test_data.txt", "r")
#data = open("15_test_data2.txt", "r")
data = open("15_data.txt", "r")

def is_hand_stronger (hand1, hand2) -> int:
    return -1

#vars outside loop
sum = 0
nodes = []
node_indexes = []
instructions = ''

for i_idx, line in enumerate(data):
    #iteration through lines
    if(i_idx == 0):
        instructions = line
    if(i_idx > 1):
        nodes.append([line[0:3], line[7:10], line[12:15]])
        node_indexes.append(line[0:3])

current_node = nodes[node_indexes.index('AAA')]
steps = 0
step_num = 0

while(current_node[0] != 'ZZZ'):
    #print(current_node, steps, instructions[step_num])
    if( instructions[step_num] == 'L' ):
       current_node = nodes[node_indexes.index(current_node[1])]
    else:
       current_node = nodes[node_indexes.index(current_node[2])]
    steps += 1
    step_num += 1
    if( step_num == len(instructions) - 1 ):
        step_num = 0

#print(instructions)
#print(nodes)
print(steps)