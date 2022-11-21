import random
mydeck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "aas", "boer", "vrouw", "heer",]
mycards = ["harten ","klaveren ","schoppen ","ruiten ",]
deck = ["joker","joker",]
for x in range(54):
    choice1 = random.choice(mycards)
    choice2 = random.choice(mydeck)
    deck.append(choice1 + choice2)
random.shuffle(deck)
for i in range(7): 
    print(deck[i])
print(deck[8:54])
