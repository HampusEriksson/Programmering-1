suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
values = ["Ace", "King", "Queen", "Jack", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
deck = []
for suit in suits:
     for value in values:
          deck.append(Card(value + " of " + suit, value))