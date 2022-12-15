from fruitmand import fruitmand
kleuren = []
for x in range (len(fruitmand)):
    fruitmand.remove({fruitmand[x].get("druif")})
    if fruit['name']=='druif':
        fruitmand.pop(fruitmand.index(fruit))
for i in range (len(fruitmand)):
    kleur = (fruitmand[i]['color'])
    if kleur not in kleuren:
        kleuren.append(kleur)
print (kleuren)