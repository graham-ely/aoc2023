#9:37 from my start of 3
#data = open("3_test_data.txt", "r")
data = open("3_data.txt", "r")
sum = 0

impossible_flag = False

for line in data:
    items = line.split();
    for idx, item in enumerate(items):
        if( item.find("red") > -1 ):
            if( int(items[idx - 1]) > 12 ):
                impossible_flag = True
        if( item.find("green") > -1 ):
            if( int(items[idx - 1]) > 13 ):
                impossible_flag = True
        if( item.find("blue") > -1 ):
            if( int(items[idx - 1]) > 14 ):
                impossible_flag = True
    if not impossible_flag:
        sum += int(items[1][0:-1])
    impossible_flag = False

print( sum )