import csv
from functools import cmp_to_key

def hand_value(hand):  
    cards = list(hand)
    counts = {}
    
    for card in cards:
        counts[card] = counts.get(card, 0) + 1
    
    pairs = [(count, card) for card, count in counts.items()] #convert to list of tuples
    
    pairs.sort(reverse=True)
    sorted_cards = [card for count, card in pairs]
    
    if len(counts) == 1:        
        hand_type = "5oK"
    elif len(counts) == 2:    
        if pairs[0][0] == 4:       
            hand_type = "4oK"
        else:           
            hand_type = "FH"
    elif len(counts) == 3:    
        if pairs[0][0] == 3:      
            hand_type = "3oK"
        else:           
            hand_type = "2p"
    elif len(counts) == 4:   
        hand_type = "1p"
    else:     
        hand_type = "HC"
    
    return (hand_type, sorted_cards)


def compare_hands(hand1, hand2):
    value1 = hand_value(hand1)
    value2 = hand_value(hand2)

    if hand_values[value1[0]] < hand_values[value2[0]]: #first hand weaker
        return -1
    elif hand_values[value1[0]] > hand_values[value2[0]]:#first hand stronger
        return 1
    else:#equal strength hand type
        for i in range(5):
            if card_values[value1[1][i]] < card_values[value2[1][i]]: #first hand, weaker card order
                return -1
            elif card_values[value1[1][i]] > card_values[value2[1][i]]:#first hand, stronger card order
                return 1
        return 0#hands are equal
    
def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        return [(row[0], int(row[1])) for row in reader]

def total_winnings(hands_and_bids):  
    hands_and_bids.sort(key=cmp_to_key(lambda x, y: compare_hands(x[0], y[0]))) 
    winnings = 0
    
    for i in range(len(hands_and_bids)):       
        hand, bid = hands_and_bids[i]      
        rank = i + 1       
        winnings += bid * rank
    return winnings

card_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
hand_values = {"5oK": 8, "4oK": 7, "FH": 6, "3oK": 5, "2p": 4, "1p": 3, "HC": 2}

hands_and_bids = [("32T3K", 765), ("T55J5", 684), ("KK677", 28), ("KTJJT", 220), ("QQQJA", 483)]

if __name__ == "__main__":

    print(total_winnings(hands_and_bids))
    
    data = read_csv('day_7_input.csv')
    print(data)
    print(total_winnings(data))
