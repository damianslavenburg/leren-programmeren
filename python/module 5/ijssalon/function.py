def intro():
    print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')

def bolletjes():

    bolletjes = int(input('Hoeveel bolletjes wilt u? '))

    if bolletjes > 8:
        print('Sorry, dat wordt te veel!')
        bolletjes = int(input('Hoeveel bolletjes wilt u? '))

    if bolletjes < 1:
        print('Sorry, dat wordt te weinig!')
        bolletjes = int(input('Hoeveel bolletjes wilt u? '))

    elif bolletjes > 3:
        print('Dan krijgt u van mij een bakje met ' + str(bolletjes) + ' bolletjes.')

    elif bolletjes >= 0 and bolletjes <= 3:
        keuze = input('wilt u een bakje of een hoorntje? ')

    if keuze == 'bakje':
        print('dan krijgt u een bakje met ' + str(bolletjes) + ' bolletjes.')
    elif keuze == 'hoorntje':
        print('dan krijgt u een hoorntje met ' + str(bolletjes) + ' bolletjes.')
    else: 
        print('Sorry, dat begrijp ik niet.')
        keuze = input('wilt u een bakje of een hoorntje? ')

    



