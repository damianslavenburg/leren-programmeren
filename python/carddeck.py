import random
mydeck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "aas", "boer", "vrouw", "heer",]
mycards = ["harten ","klaveren ","schoppen ","ruiten ",]
deck = ["joker","joker",]
for x in range(len(mycards)):
    for l in range(len(mydeck)):
        combi = mycards[x] + mydeck[l]
        deck.append(combi)
random.shuffle(deck)
for i in range(7): 
    print(deck[i])
print(deck[7:54])
