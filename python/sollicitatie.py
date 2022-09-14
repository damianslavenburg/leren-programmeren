print("--------------------------------------------------------------")
print("sollicteer formuleer: Circusdirecteur voor Circus HotelDeBotel")
print("--------------------------------------------------------------")
print("we gaan u een aantal vragen stellen die te maken hebben met")
print("de sollitatie")
print("--------------------------------------------------------------")

naam = input("wat is u naam?").lower()

ervaring = input("heeft u ervaring met dieren, jongleren of acrobatiek?").lower()
if ervaring  == "dieren" : 
 jaar_ervaring = input("en hoeveel jaar?")
elif ervaring == "jongleren" :
 jaar_ervaring = input("en hoeveel jaar?")
elif ervaring == "acrobatiek" :
    jaar_ervaring = input("en hoeveel jaar?")



diploma = input("welke diploma heeft u?").lower()
geslacht = input("bent u een man of een vrouw?").lower()

if geslacht == "man":
    print(" hoe breed is u snor?")
    lengte_haar = input().lower()
elif geslacht == "vrouw": 
    print("hoe lang is u krullend haar?")
    lengte_haar = input().lower()

rijbewijs = input("welke rijbewijs bezit u?").lower()
hoed = input("bent u in bezit van een hoge hoed?").lower()
gewicht = input("hoeveel weegt u?").lower()
lengte = input("hoe lang bent u?")
certificaat= input("heeft u een certificaat van overleven met gevaarlijk personeel?").lower()
random_vraag_1 = input("hou oud zijn je ouders?")
random_vraag_2 = input("heb je een broer of zus?")
random_vraag_3 = input("heb je huis dieren?")
random_vraag_4 = input("waar ben je geboren?")

goed = False
if ervaring == "dieren" or "jongleren" or "acrobatiek" :
    if jaar_ervaring == "4" or "5" or "3" :
        if diploma == "mbo-4":
            if lengte_haar == "10 cm" or "20 cm":
                if rijbewijs == "vrachtwagen":
                    if hoed == "ja":
                        if lengte == "150":
                            if gewicht == "90": 
                                if certificaat == "ja":
                                    goed = True
                                    print("gefeliciteerd u bent in aanraking met de baan :Circusdirecteur voor Circus HotelDeBotel stuur snel u cv op.")
if goed == False:
    print("sorry u komt niet in aanraking met de baan Circusdirecteur voor Circus HotelDeBotel.")                                   

