import random
bomb = random.randint(1,3)
score = 0
play = True
ronde = 1
while play == True:
        guess = input("u are at round " + str(ronde) + " choose random number: ")
        
        try:
                int(guess)
                if int(guess) == bomb:
                        play = False
                        print("game over bomb exploded")
        
                elif int(guess) < 1: 
                        print('less than 1 is no possible')
                        play = True

                elif int(guess) > 10 :
                        print('more than 10 is not possible')
                        play = True
                else: 
                        score = score + (ronde * ronde)
                        ronde = ronde + 1
                        print("u are safe")
                        nextronde = input('do you want to go to round '+ str(ronde) +'(y/n)').lower()
                        play = True
                        if nextronde == "no" or "n":
                                play = False
        except:
                print('that is not a number')

               
print('your score is', score)
                