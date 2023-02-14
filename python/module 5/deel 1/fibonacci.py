import random

def fibonaci(aantal:int):
    fibonacci = []
    var1 = 0
    var2 = 1
    fibonacci.append(var1)
    fibonacci.append(var2)
    aantal = aantal - 2

    for i in range(aantal):
        fibonacci.append(fibonacci[var1] + fibonacci[var2])
        var1 = var1 + 1 
        var2 = var2 + 1 

    return fibonacci


aantal = input("Hoeveel getallen will je? ")

print(fibonaci(int(aantal)))