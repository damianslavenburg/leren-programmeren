# name of student: damian slavenburg
# number of student: 99072083
# purpose of program: wisselgeld tellen
# function of program: kiezen welke munten je terug wilt
# structure of program:  python
toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #
vijf_euro = 0
drie_euro = 0
twee_euro = 0
vijftig_cent = 0
twintig_cent = 0
tien_cent = 0
vijf_cent = 0
twee_cent = 0
een_cent = 0

if change > 0: #
  coinValue = 500 #

  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #
    if coinValue == 500:
      vijf_euro = vijf_euro+1 * nrCoinsReturned
    elif coinValue == 300:
      drie_euro = drie_euro+1 * nrCoinsReturned
    elif coinValue == 200:
      twee_euro = twee_euro+1 * nrCoinsReturned
    elif coinValue == 50:
      vijftig_cent = vijftig_cent+1 * nrCoinsReturned
    elif coinValue == 20:
      twintig_cent = twintig_cent+1 * nrCoinsReturned
    elif coinValue == 10:
      tien_cent = tien_cent+1 * nrCoinsReturned
    elif coinValue == 5:
      vijf_cent = vijf_cent+1 * nrCoinsReturned
    elif coinValue == 2:
      twee_cent = twee_cent+1 * nrCoinsReturned
    elif coinValue == 1:
      een_cent = een_cent+1 * nrCoinsReturned
# comment on code below: welke soort munt
  if coinValue == 500:
      coinValue = 300
  elif coinValue == 300:
      coinValue=200
  elif coinValue == 200:
      coinValue = 50
  elif coinValue == 50:
      coinValue = 20
  elif coinValue == 20:
      coinValue = 10
  elif coinValue == 10:
      coinValue = 5
  elif coinValue == 5:
      coinValue=2
  elif coinValue == 2:
      coinValue = 1
  else:
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')
  print("U heeft ",vijf_euro,"munten van vijf euro en ",drie_euro,"munten van drie euro en",twee_euro,"munten van twee euro en",vijftig_cent,"munten van vijftig cent en",twintig_cent,"munten van drie euro en",tien_cent,"munten van tien cent en",vijf_cent,"munten van vijf cent en",twee_cent,"munten van twee cent en",een_cent,"munten van een cent")