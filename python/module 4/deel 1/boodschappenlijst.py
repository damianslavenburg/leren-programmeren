lijst = {}
repeat = True

while repeat == True:
    item = input("Wat wil je nog aan je boodschappen lijst toevoegen? ").lower()
    aantal = int(input("Hoeveel wil je daarvan? "))

    if item in lijst:
            lijst[item] = lijst[item] + aantal


    else:
            lijst[item] = aantal

    herhalen = input("Wilt u nog meer toevoegen?").lower()

    if herhalen == "yes" or herhalen == "ja":
        repeat = True

    elif herhalen == "no" or herhalen == "nee":
        repeat = False


        print("Hier is jou lijst:")
        print("---------------------------")
        for key, value in lijst.items():
            print(value,"x ",key)
        print("---------------------------")