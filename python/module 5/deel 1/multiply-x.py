def multiplier(num):
    for i in range(1, 11):
        print(f"{i} x {num} = {num*i}")

getal = int(input("Van welk getal wilt u de tafel zien? "))
multiplier(getal)
