
all_dagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")
all_dagenreversed = reversed(all_dagen)

all_dagenreversed = tuple(all_dagenreversed)

werkdagen = reversed(all_dagen[0:5])
werkdagen = tuple(werkdagen)

weekend = reversed(all_dagen[5:7])
weekend = tuple(weekend)    

print(all_dagen)
print(all_dagen[0:5])
print(all_dagen[5:7])
print(all_dagenreversed)
print(werkdagen)
print(weekend)
