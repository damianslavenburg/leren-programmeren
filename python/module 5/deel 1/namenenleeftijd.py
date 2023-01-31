def vraag_persoon_gegevens():
    naam = input("Voer naam in: ")
    leeftijd = input("Voer leeftijd in: ")
    return {'naam': naam, 'leeftijd': leeftijd}

persoon_lijst = []
while True:
    persoon = vraag_persoon_gegevens()
    persoon_lijst.append(persoon)
    verder_gaan = input("Druk op enter om door te gaan of typ 'stop' om te printen: ")
    if verder_gaan.lower() == 'stop':
        break

for persoon in persoon_lijst:
    print("Naam:", persoon['naam'], "Leeftijd:", persoon['leeftijd'])
