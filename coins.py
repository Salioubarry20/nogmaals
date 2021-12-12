# name of student: Saliou Barry
# number of student: 99052276
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # ariabele toPay is een getal die met decimale kan werken waar je in kan vullen wat je moet betalen x 100
paid = int(float(input('Paid amount: ')) * 100) # ariabele toPay is een getal die met decimale kan werken waar je in kan vullen wat je moet betalen x 100
change = paid - toPay # variabele bereken paid en toPay en dat is dan de variabele van change

if change > 0: # als change groter is dan 0 voer de code onder de if uit
  coinValue = 50 # variabele coinValue waarde is 500
  
  while change > 0 and coinValue > 0: # zolang change groter is dan 0 en coinValue ook groter is dan 0
    nrCoins = change // coinValue # nrCoins word de gehele waarden van change en coinValue

    if nrCoins > 0: # als nrCoins groter is dan 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # print de text
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # laat de aantal munten zien die ze moeten betalen en geef een input waar ze het aantal in kunnen vullen
      change -= nrCoinsReturned * coinValue # doe change - nrCoinsReturned x coinValue en dat word de nieuwe waarde van de variabele

# comment on code below: als coinValue 50 is maak het dan 20 als het 20 is maak het 10 etc
    if coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else: 
      coinValue = 0

if change > 0: # als change groter is dan 0 print de text hieronder
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done') 