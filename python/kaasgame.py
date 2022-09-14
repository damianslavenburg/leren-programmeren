

repeat = True

while repeat == True:
    print("is de kaas geel?")
    vraag = input().lower()
    
    if vraag == "ja":
        repeat = False
        print("zitten er gaten in?")
        vraag=input().lower()

        if vraag == "ja":
            repeat = False
            print("is de kaas belagelijk duur?")
            vraag = input().lower()
            if vraag == "ja":
                repeat = False
                print("dan is de kaas emmenthaler")
            elif vraag == "nee":
                repeat = False
                print("de kaas is dan leerdammer kaas") 
        
        elif vraag == "nee":
            repeat = False
            print("is de kaas hard als een steen?")
            vraag = input().lower() 
            if vraag == "ja":
                repeat = False
                print("dan is de kaas parmigiano reggiano")
            if vraag == "nee":
                repeat = False
                print("dan is de kaas goudse kaas")

    elif vraag == "nee":
        repeat = False
        print("heeft de kaas blauwe schimmel?")
        vraag=input().lower()

        if vraag == "ja":
            repeat = False
            print("heeft de kaas een korst?")
            vraag = input().lower()
            if vraag == "ja":
                repeat = False
                print("dan is de kas blue de rochbaron")
            elif vraag == "nee":
                repeat = False
                print("dan is de kaas foume d'ambert") 
        
        elif vraag == "nee":
            repeat = False
            print("heeft de kaas een korst?")
            vraag = input().lower() 
            if vraag == "ja":
                repeat = False
                print("dan is de kaas camembert")
            if vraag == "nee":
                repeat = False
                print("dan is de kaas mozzarella")
else: 
    repeat = True
    

