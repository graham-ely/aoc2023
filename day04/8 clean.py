# 30:28 from my start of 7
# + 5 minutes rewrote this after to not use such an ugly, slow nested loop process
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
    items.pop(0)
    card_number += int(items.pop(0)[0:-1])
    if( card_number in card_copies ):
        card_copies.update({card_number: card_copies.get(card_number) + 1})
    else:
        card_copies.update({card_number: 1})    
    print(card_number)
    #iteration through lines
    for idx, item in enumerate(items):
        #iteration through line if needed
        if( item == '|'):
            line_flag = True
        elif( line_flag ):
            if( item in winning_numbers ):
                matches+=1
        else:
            winning_numbers.append(item)
    num_cards = 1
    if(card_number in card_copies):
        num_cards = card_copies.get(card_number)
    #handle current card
    card_number += 1
    for x in range(matches):
        if( card_number in card_copies ):
            card_copies.update({card_number: card_copies.get(card_number) + num_cards})
        else:
            card_copies.update({card_number: num_cards})    
        card_number += 1
    
    winning_numbers = []
    matches = 0
    card_score = 0
    line_flag = False
    card_number = 0

for card, card_value in card_copies.items():
    print(card, card_value)
    sum += card_value

print( sum )