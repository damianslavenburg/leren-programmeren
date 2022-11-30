boodschappen = {}
repeat = True

while repeat == True:
    item = input("Wat wil je nog aan je boodschappen lijst toevoegen? ").lower()
    aantal = int(input("Hoeveel wil je daarvan? "))

    if item in boodschappen:
            boodschappen[item] = boodschappen[item] + aantal


    else:
            boodschappen[item] = aantal

    herhalen = input("Wilt u nog meer toevoegen?").lower()

    if herhalen == "yes" or herhalen == "ja":
        repeat = True

    elif herhalen == "no" or herhalen == "nee":
        repeat = False


        print("Hier is jou lijst:")
        print("---------------------------")
        for key, value in boodschappen.items():
            print(value,"x ",key)
        print("---------------------------")