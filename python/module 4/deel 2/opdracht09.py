from fruitmand import fruitmand
fruitmand.remove({    
    'name' : 'druif',
    'weight' : 5,
    'color' : 'red',
    'round' : True})
for fruit in  range (len(fruitmand)):
  print(fruitmand[fruit]['color'])