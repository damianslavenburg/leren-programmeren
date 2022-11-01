# vraag voor de naam van persoon
naam = input("wat is je naam?")
# print de naam en vragen hoe het gaat
vraag = input("hoi " + naam + " hoe is het? ")
if vraag == 'goed':
    print('dat is mooi')
# vragen hoe zo het niet goed gaat
else: 
    input('hoezo gaat het niet goed? ')
    print(naam ," dat is niet leuk")