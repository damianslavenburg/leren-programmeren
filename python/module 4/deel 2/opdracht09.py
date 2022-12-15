from fruitmand import fruitmand
kleuren = []
for i in range (len(fruitmand)):
    kleur = (fruitmand[i]['color'])
    if kleur not in kleuren:
        kleuren.append(kleur)
print(kleuren)
