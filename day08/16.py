from functools import cmp_to_key
from math import lcm

# 1:20:04 from my start of 15
#data = open("15_test_data.txt", "r")
#data = open("15_test_data2.txt", "r")
data = open("15_data.txt", "r")

def is_hand_stronger (hand1, hand2) -> int:
    return -1

#vars outside loop
sum = 0
nodes = []
node_indexes = []
start_nodes  = []
end_nodes    = []
instructions = ''

for i_idx, line in enumerate(data):
    #iteration through lines
    if(i_idx == 0):
        instructions = line
    if(i_idx > 1):
        nodes.append([line[0:3], line[7:10], line[12:15]])
        node_indexes.append(line[0:3])
        if(line[2] == 'A'):
            start_nodes.append([line[0:3], line[7:10], line[12:15]])
        if(line[2] == 'Z'):
            end_nodes.append([line[0:3], line[7:10], line[12:15]])

print(start_nodes)
print(end_nodes)
end_nodes_dists = []

for start_node in start_nodes:
    ends = []
    current_node = start_node
    steps = 0
    step_num = 0
    #for x in range(10):

    while(len(ends) < 10):
        if( current_node in end_nodes ):
            ends.append(steps)
        #print(current_node, steps, instructions[step_num])
        if( instructions[step_num] == 'L' ):
            current_node = nodes[node_indexes.index(current_node[1])]
        else:
            current_node = nodes[node_indexes.index(current_node[2])]
        steps += 1
        step_num += 1
        if( step_num == len(instructions) - 1 ):
            step_num = 0
        
    end_nodes_dists.append(ends)

lcm_array = []
for end_nodes_dist in end_nodes_dists:
    lcm_array.append(end_nodes_dist[0])

print(lcm_array)
# grabbed these values manually from line above since lcm doesn't want a list
print(lcm(21883, 19667, 14681, 16897, 13019, 11911))

#print(instructions)
#print(nodes)
print(steps)