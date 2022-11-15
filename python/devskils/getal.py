list =[]
number = 0

for x in range(20):
    nummer = input("getal: ")
    list.append(nummer)
    if int(nummer) % 3 == 0:
        number = number + 1
list.sort()
print(list[0],list[-1])
print(number)