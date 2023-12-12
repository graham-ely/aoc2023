# 30:28 from my start of 7
#data = open("7_test_data.txt", "r")
data = open("7_data.txt", "r")

#vars outside loop
sum = 0
matches = 0
card_score = 0
winning_numbers = []
line_flag = False
card_copies = {}
card_number = 0

for line in data:
    items = line.split();
    #remove cards and game number
    #card_number = items.pop(0) + ' '
    items.pop(0)
    card_number += int(items.pop(0)[0:-1])
    if( card_number in card_copies ):
        card_copies.update({card_number: card_copies.get(card_number) + 1})
    else:
        card_copies.update({card_number: 1})    
    print(card_number)
    #iteration through lines
    for x in range(card_copies.get(card_number)):
        for idx, item in enumerate(items):
            #iteration through line if needed
            if( item == '|'):
                line_flag = True
            elif( line_flag ):
                if( item in winning_numbers ):
                    matches+=1
                    #if( matches == 1 ):
                        #card_score = 1
                    #else:
                        #card_score *= 2
            else:
                winning_numbers.append(item)
        #handle current card
        c_card_number = card_number + 1
        for x in range(matches):
            if( c_card_number in card_copies ):
                card_copies.update({c_card_number: card_copies.get(c_card_number) + 1})
            else:
                card_copies.update({c_card_number: 1})    
            c_card_number += 1
        
        winning_numbers = []
        matches = 0
        card_score = 0
        line_flag = False
        c_card_number = 0
    card_number = 0

for card, card_value in card_copies.items():
    print(card, card_value)
    sum += card_value
    #iterate vars oustside loop
    #clear flags

print( sum )