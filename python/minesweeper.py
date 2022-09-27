import random
bomb = random.randint(1,10)
score = 0
play = True
ronde = 1
while play == True:
        guess = input("u are at round " + str(ronde) + " choose random number: ")

        if int(guess) == bomb:
                play = False
                print("game over bomb exploded")
        
        else: 
                score = score + (ronde * ronde)
                ronde = ronde + 1
                print("u are safe")
                nextronde = input('wilt u naar ronde '+ str(ronde) +'(y/n)')
                play = True
                if nextronde == "n":
                        play = False
print('your score is', score)