# 51:10 from my start of 13
#data = open("13_test_data.txt", "r")
data = open("13_data.txt", "r")

card_values = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 11,
    'T' : 10,
    '9' : 9,
    '8' : 8,
    '7' : 7,
    '6' : 6,
    '5' : 5,
    '4' : 4,
    '3' : 3,
    '2' : 2,
}
hand_values = {
    '5k' : 7,
    '4k' : 6,
    'fh' : 5,
    '3k' : 4,
    '2p' : 3,
    '1p' : 2,
    'hi' : 1
}

def get_hand_str (hand) -> int:
    fh2_flag = False
    fh3_flag = False
    p2_flag  = False

    for card in card_values:
        card_count = hand.count(card)

        if(card_count == 5):
            return hand_values.get('5k')
        if(card_count == 4):
            return hand_values.get('4k')
        if(card_count == 3):
            #print('3', hand, card)
            if( fh2_flag is True ):
                return hand_values.get('fh')
            fh3_flag = True
        if(card_count == 2):
            if( fh3_flag is True ):
                return hand_values.get('fh')
            elif( p2_flag is True ):
                return hand_values.get('2p')
            fh2_flag = True
            p2_flag = True

    if( fh3_flag is True ):
        return hand_values.get('3k')
    elif( p2_flag is True or fh2_flag is True):
        return hand_values.get('1p')
    else:
        return hand_values.get('hi')

def is_hand_stronger (hand1, hand2) -> bool:
    hand1_str = get_hand_str(hand1)
    hand2_str = get_hand_str(hand2)

    if (hand1_str > hand2_str):
        return True
    elif (hand2_str > hand1_str):
        return False
    else:
        for x in range(len(hand1)):
            if (card_values.get(hand1[x]) > card_values.get(hand2[x])):
                return True
            elif (card_values.get(hand2[x]) > card_values.get(hand1[x])):
                return False

    return False

#vars outside loop
sum = 0
hands = []

for i_idx, line in enumerate(data):
    #iteration through lines
    items = line.split()
    hands.append([items[0], items[1]])

ranked_hands = []

current_rank = len(hands)
while(len(hands) > 0):
    current_hand = hands[0]
    print(current_hand[0], get_hand_str(current_hand[0]))
    for x in range(len(hands)):
        if(is_hand_stronger(current_hand[0], hands[x][0]) is False):
            current_hand = hands[x]
    hands.remove(current_hand)
    current_hand.append(current_rank)
    ranked_hands.append(current_hand)
    current_rank -= 1

for hand, bid, rank in ranked_hands:
    sum += int(bid) * int(rank)

print(sum)