# 19:30 from my start of 11
#data = open("12_test_data.txt", "r")
data = open("12_data.txt", "r")

def race_time(time, record) -> int:
    num_over_record = 0
    for x in range(time):
        attempt = x * (time - x)
        if attempt > record:
            num_over_record += 1
    
    return num_over_record

#vars outside loop
sum = 0
races = []

for i_idx, line in enumerate(data):
    #iteration through lines
    items = line.split()
    items.pop(0)
    races.append(items)
    #for idx, item in enumerate(items):
    #    #iteration through line if needed
    #    races
    #iterate vars oustside loop
    #clear flags
races = list(zip(races[0], races[1]))
print(races)

num_ways = 1
for time, record in races:
    num_ways *= race_time(int(time), int(record))


print(races)
print( num_ways )