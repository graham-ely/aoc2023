from functools import cmp_to_key
from math import lcm

#  from my start of 21
data = open("21_test_data.txt", "r")
#data = open("21_data.txt", "r")

def find_extrapolated_value (items, last_val) -> int:
    return -1

#vars outside loop
sum = 0
hands = []

for i_idx, line in enumerate(data):
    #iteration through lines
    items = list(map(int, line.split()))
    #print(sum)

print(sum)