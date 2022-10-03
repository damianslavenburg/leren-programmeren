repeat = True
aantal = 0


while repeat == True:
    quit = input("?")
    aantal = aantal + 1
    repeat = True
    
    if quit == "quit":
        repeat = False
        print(aantal)
        exit()
