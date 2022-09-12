print("voer het eerste getal in:")
a= input()
print("voer het tweede getal in:")
b= input()
 #1
if a > b:
    max = a
    min = b
    print("a is het grootste getal:", max)
 #2
elif a < b:
    min = a
    max = b 
    print("a is het kleinste getal:", min)
 #3
else:
    print("a en b zijn even groot")
 #4
print("Het minimum is:", str(min))
print("Het maximum is:", str(max))

