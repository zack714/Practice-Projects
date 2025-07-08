#this program uses pyinputplus to simulate a sandwich shop.
#7/7/2025

import pyinputplus as pyip
itemPrices = {'bread':{'white':1.00, 'wheat':1.25,'sourdough':2.00},'protein':{'chicken':2.00,'turkey':2.50,'ham':2.00,'tofu':3.50},
'cheese':{'cheddar':0.50,'swiss':1.25,'mozzarella':1.00}}

totPrice = 0.0

print("Hello! Welcome to Christian Aruba's sandwich shop.")
breadRes = pyip.inputMenu(['white','wheat','sourdough'])

print("Now, select a protein.")
proRes = pyip.inputMenu(['chicken','turkey','ham','tofu'])

cheeseRes = pyip.inputYesNo("Would you like cheese?")

if cheeseRes != 'no':
    cheeseRes = pyip.inputMenu(['cheddar','swiss','mozzarella'])
else:
    cheeseRes = 0.0

extraRes = pyip.inputYesNo('Would you like mayo, mustard, lettuce, or tomato?')

numSands = pyip.inputInt('How many sandwiches would you like?')

breadPrice = itemPrices.get("bread",0.0).get(breadRes,0.0)
proteinPrice = itemPrices.get("protein",0.0).get(proRes,0.0)
cheesePrice = itemPrices.get('cheese',0.0).get(cheeseRes,0.0)
totPrice += breadPrice + proteinPrice + cheesePrice

if extraRes!= 'no':
    totPrice+=.50

totPrice*=numSands

print(f"Your total price with {numSands} sanwiches is ${totPrice}.")