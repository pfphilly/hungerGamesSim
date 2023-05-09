import csv
import random
print("THE HUNGER GAMES")

print("enter the values below 1 to 10")
print("enter by puting name then stringth then friendlyness then smarts then sponsor popularity separated by commas. when you are done enter 'May The Odds Be Ever In Your Favor' capitalized just like that")


players = []

#with open('players.csv') as csvfile:
#    reader = csv.DictReader(csvfile)
#    for row in reader:
#        players.append(row)

players = {
    'peter' : {'strength' : 5, 'friendlyness' : 8, 'smarts' : 10, 'sponsor_popularity' : 9, 'special_trait' : 5},
    'jonathan' : {'strength' : 4, 'friendlyness' : 8, 'smarts' : 10, 'sponsor_popularity' : 8, 'special_trait' : 1},
    'avni' : {'strength' : 2, 'friendlyness' : 9, 'smarts' : 10, 'sponsor_popularity' : 7, 'special_trait' : 5},
    'izzy' : {'strength' : 7, 'friendlyness' : 8, 'smarts' : 8, 'sponsor_popularity' : 9, 'special_trait' : 4}
}
print("LET THE GAMES BEGIN")
for player in players:
    if player["smarts"] == 0 or player["smarts"] == 1:
        chanceOfDeath = random.randint(0,10)
        if chanceOfDeath == 7:
            print(player["name"] + "Was a little jumpy and left their circle before the gong and steped on a land mine.")

