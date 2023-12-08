from functools import cmp_to_key
from math import lcm

# 51:10 from my start of 13
data = open("17_test_data.txt", "r")
#data = open("17_data.txt", "r")

def is_hand_stronger (hand1, hand2) -> int:
    return -1

#vars outside loop
sum = 0
hands = []

for i_idx, line in enumerate(data):
    #iteration through lines
    items = line.split()
    hands.append([items[0], items[1]])

print(sum)