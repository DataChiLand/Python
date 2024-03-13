import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards) 

"""Returns a random card from the deck"""

user_cards = []
computer_cards = []
is_game_over = False

for _ in range (2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else: 
        user_should_deal = input("Type 'y' to get another cards, type 'n' to pass ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True
          


