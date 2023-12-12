# 7:51 from my start of 7
#data = open("7_test_data.txt", "r")
data = open("7_data.txt", "r")

#vars outside loop
sum = 0
matches = 0
card_score = 0
winning_numbers = []
line_flag = False

for line in data:
    items = line.split();
    #remove cards and game number
    items.pop(0)
    items.pop(0)
    print(items)
    #iteration through lines
    for idx, item in enumerate(items):
        #iteration through line if needed
        if( item == '|'):
            line_flag = True
        elif( line_flag ):
            if( item in winning_numbers ):
                matches+=1
                if( matches == 1 ):
                    card_score = 1
                else:
                    card_score *= 2
        else:
            winning_numbers.append(item)
    sum += card_score
    winning_numbers = []
    matches = 0
    card_score = 0
    line_flag = False

    #iterate vars oustside loop
    #clear flags

print( sum )