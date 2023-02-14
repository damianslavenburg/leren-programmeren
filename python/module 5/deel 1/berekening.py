def addition(n1:int, n2 = 1):
    return n1 + n2

def subtraction(n1:int, n2 = 1):
    return n1 - n2

def multiplication(n1:int, n2 = 2):
    return n1 * n2 

def division(n1:int, n2 = 2):
    return n1 / n2



print("""
    wat wilt u doen?
    (A) getallen optellen,
    (B) getallen aftrekken,
    (C) getallen vermenigvuldigen,
    (D) getallen delen,
    (E) getal ophogen,
    (F) getal verlagen,
    (G) getal verdubbelen,
    (H) getal halveren.
    """)

geen = ["e", "f", "g", "h"]
wel = ["a", "b", "c", "d"]
repeat = True

n1 = int(input("voer een getal in: "))

while repeat == True:
    
    keuze = input("taak: ").lower()


    if keuze in wel :
        n2 = int(input("voer een tweede getal in: "))


        if keuze == "a":
            n3 = (addition(n1,n2))
            print(n3)

        if keuze == "b":
            n3 = (subtraction(n1,n2))
            print(n3)

        if keuze == "c":
            n3 = (multiplication(n1,n2))
            print(n3)

        if keuze == "d":
            n3 = (division(n1,n2))
            print(n3)
    
    
    elif keuze in geen:

        if keuze == "e":
            n3 =(addition(n1))
            print(n3)

        if keuze == "f":
            n3 =(subtraction(n1))
            print(n3)

        if keuze == "g":
            n3 =(multiplication(n1))
            print(n3)

        if keuze == "h":
            n3 =(division(n1))
            print(n3)

    if keuze == "stop":
        quit()

    
    n1 = n3
