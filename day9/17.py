from functools import cmp_to_key
from math import lcm

# 18:25 from my start of 17
#data = open("17_test_data.txt", "r")
data = open("17_data.txt", "r")

def find_extrapolated_value (items, last_val) -> int:
    new_vals = []
    for idx, item in enumerate(items):
        if( idx == 0 ):
            continue
        else:
            new_vals.append(item - items[idx - 1])
    if( len(set(new_vals)) == 1 ):
        print("true", new_vals[0] + last_val)
        return new_vals[0] + last_val
    else:
        return find_extrapolated_value(new_vals, new_vals[len(new_vals) - 1]) + last_val

#vars outside loop
sum = 0
hands = []

for i_idx, line in enumerate(data):
    #iteration through lines
    items = list(map(int, line.split()))
    sum += find_extrapolated_value(items, items[len(items) - 1]) 
    #print(sum)

print(sum)