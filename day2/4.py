#13:15 from my start of 3
#data = open("3_test_data.txt", "r")
data = open("3_data.txt", "r")
sum = 0

max_red = 0
max_green = 0
max_blue = 0

for line in data:
    items = line.split();
    for idx, item in enumerate(items):
        if( item.find("red") > -1 ):
            if( int(items[idx - 1]) > max_red ):
                max_red = int(items[idx - 1])
        if( item.find("green") > -1 ):
            if( int(items[idx - 1]) > max_green ):
                max_green = int(items[idx - 1])
        if( item.find("blue") > -1 ):
            if( int(items[idx - 1]) > max_blue ):
                max_blue = int(items[idx - 1])
    power = max_red * max_blue * max_green
    sum += power
    max_red = 0
    max_blue = 0
    max_green = 0

print( sum )