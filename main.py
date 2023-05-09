import csv
import random
import numpy
print("THE HUNGER GAMES")

#print("enter the values below 1 to 10")
#print("enter by puting name then stringth then friendlyness then smarts then sponsor popularity separated by commas. when you are done enter 'May The Odds Be Ever In Your Favor' capitalized just like that")


players = []

#with open('players.csv') as csvfile:
#    reader = csv.DictReader(csvfile)
#    for row in reader:
#        players.append(row)

players = {
    'peter' : {'name' : 'peter', 'strength' : 5, 'friendlyness' : 8, 'smarts' : 10, 'sponsor_popularity' : 9, 'special_trait' : 5},
    'jonathan' : {'name' : 'jonathan', 'strength' : 4, 'friendlyness' : 8, 'smarts' : 10, 'sponsor_popularity' : 8, 'special_trait' : 1},
    'avni' : {'name' : 'avni', 'strength' : 2, 'friendlyness' : 9, 'smarts' : 10, 'sponsor_popularity' : 7, 'special_trait' : 5},
    'izzy' : {'name' : 'izzy', 'strength' : 7, 'friendlyness' : 8, 'smarts' : 8, 'sponsor_popularity' : 9, 'special_trait' : 4},
    'luca' : {'name' : 'luca', 'strength' : 8, 'friendlyness' : 6, 'smarts' : 10, 'sponsor_popularity' : 1, 'special_trait' : 18},
    'alden' : {'name' : 'alden', 'strength' : 10, 'friendlyness' : 6, 'smarts' : 9, 'sponsor_popularity' : 8, 'special_trait' : 19 }
}
print("LET THE GAMES BEGIN")

for player in players:
    smarts = players.get(player).get('smarts')
    if smarts == 0 or smarts == 1:
        chanceOfDeath = random.randint(0,10)
        print(chanceOfDeath)
        if chanceOfDeath == 7:
            print(f"{players.get(player).get('name')} Was a little jumpy and left their circle before the gong and steped on a land mine.")


print("BLOODBATH:\n")
bloodbath = []
cornicopiaWeapons = numpy.array['axe', 'axe', 'axe', 'hatchet', 'hatchet', 'knife', 'knife', 'knife', 'knife', 'knife', 'knife', 'knife', 'knife', 'bowArrows', 'bowArrows', 'handgun', 'spear', 'spear', 'darts', 'darts', 'battle axe', 'sling', 'sling', 'sword', 'sword', 'sword']
cornicopiaItems = numpy.array['medkit', 'medkit', 'medkit', 'largeRation', 'largeRation', 'smallRation', 'smallRation', 'smallRation', 'smallRation', 'smallRation', 'tarp', 'tarp', 'tarp', 'tarp', 'tarp', 'tarp', 'backpackLarge', 'backpackSmall', 'backpackSmall']
for player in players:
    if players.get(player).get('smarts') < 6 or players.get(player).get('strength') > 7:
        bloodbath.append(player)

