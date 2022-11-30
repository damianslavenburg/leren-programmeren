lijst = ['Maserati','Mazda','Mercedes-Benz','MG','Mini']

for x in range(5):

    print(lijst[x])
    

tuple = ('Maserati','Mazda','Mercedes-Benz','MG','Mini')
for x in range(5):
    print(tuple[x])


mydict = {
    "ford":"mustang",
    'opel':"astra",
    "peugot":"307",
    "volgwagen":"golf",
    "zutroen":"x3"
}
for key, value in mydict.items():
        print(key)
for key, value in mydict.items():
    print(key,value)  
