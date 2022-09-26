import random
print("hello to minesweeper")
play = input('do you want to play minesweeper?')

while play == "yes" :
        vraag = print("choose a number between 1-10: ")
        number = input()
        trueOrFalse = random.randint(0,1)
        bomb = 0
      
        if trueOrFalse:
                print('there is no bomb here')
                repeat = False
                print('you won')
        
      

        
        if not trueOrFalse:
                repeat = False
                print("bomb exploded")
        
        agian = input("do you want to play agian?")
        if agian == "yes": 
                repeat = False
        if agian == 'no': 
                  exit()
        

else: 
 exit()