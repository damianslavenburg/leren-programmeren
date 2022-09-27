play = True
ronde = 1
while play == True:

    agian = input("wilt u naar ronde "+ str(ronde))
    
    if agian == 'yes':
        play = True
        ronde = ronde + 1
    else:
        print('oke')
        play = False	
pass
