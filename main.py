import csv
import random
import numpy
#make classes for all items
class weapon:
    owner = ""
class sword(weapon):
    #1-10
    attack = 7
    defense = 5
    #1-10
    tradeValue = 7
    name = "sword"
    actionType = "slashed"

class bow_and_arrows(weapon):
    #1-10
    attack = 8
    defense = 1
    #1-10
    tradeValue = 8
    name = "bow and arrows"
    actionType = "shot"

class spear(weapon):
    attack = 7
    defense = 1
    tradeValue = 5
    name = "spear"
    actionType = "impaled"

class net(weapon):
    attack = 3
    defense = 3
    tradeValue = 2
    name = "net"
    actionType = "caught"
    specialEffect = 1

class sling(weapon):
    attack = 5
    defense = 0
    tradeValue = 1
    name = "sling"
    actionType = "shot"
    specialEffect = 2

class dart(weapon):
    attack = 4
    defense = 0
    tradeValue = 0
    name = "blow darts"
    actionType = "shot"

class knife(weapon):
    attack = 7
    defense = 2
    tradeValue = 3
    name = "knife"
    actionType = "stabbed"

class hatchet(weapon):
    attack = 8
    defense = 3
    tradeValue = 5
    name = "hatchet"
    actionType = "mauled"

hatchet1 = hatchet()
hatchet2 = hatchet()
knife1 = knife()
knife2 = knife()
knife3 = knife()
knife4 = knife()
knife5 = knife()
knife6 = knife()
knife7 = knife()
knife8 = knife()
bow_and_arrows1 = bow_and_arrows()
bow_and_arrows2 = bow_and_arrows()
spear1 = spear()
spear2 = spear()
darts1 = dart()
darts2 = dart()
sling1 = sling()
sling2 = sling()
sword1 = sword()
sword2 = sword()
sword3 = sword()
print("THE HUNGER GAMES")

#print("enter the values below 1 to 10")
#print("enter by puting name then stringth then friendlyness then smarts then sponsor popularity separated by commas. when you are done enter 'May The Odds Be Ever In Your Favor' capitalized just like that")


players = []

#with open('players.csv') as csvfile:
#    reader = csv.DictReader(csvfile)
#    for row in reader:
#        players.append(row)
#dictionary for all players
players = {
    'peter' : {'name' : 'peter', 'strength' : 5, 'friendlyness' : 8, 'smarts' : 10, 'sponsor_popularity' : 9, 'special_trait' : 5},
    'jonathan' : {'name' : 'jonathan', 'strength' : 4, 'friendlyness' : 8, 'smarts' : 10, 'sponsor_popularity' : 8, 'special_trait' : 1},
    'avni' : {'name' : 'avni', 'strength' : 2, 'friendlyness' : 9, 'smarts' : 10, 'sponsor_popularity' : 7, 'special_trait' : 5},
    'izzy' : {'name' : 'izzy', 'strength' : 7, 'friendlyness' : 8, 'smarts' : 8, 'sponsor_popularity' : 9, 'special_trait' : 4},
    'luca' : {'name' : 'luca', 'strength' : 8, 'friendlyness' : 6, 'smarts' : 10, 'sponsor_popularity' : 1, 'special_trait' : 18},
    'alden' : {'name' : 'alden', 'strength' : 10, 'friendlyness' : 6, 'smarts' : 9, 'sponsor_popularity' : 8, 'special_trait' : 19 },
    'james H' : {'name' : 'james H', 'strength' : 6, 'friendlyness' : 10, 'smarts' : 3, 'sponsor_popularity' : 5, 'special_trait' : 18},
    'james JB' : {'name' : 'james JB', 'strength' : 9, 'friendlyness' : 8, 'smarts' : 6, 'sponsor_popularity' : 8, 'special_trait' : 6},
    'julien' : {'name' : 'julien', 'strength' : 1, 'friendlyness' : 3, 'smarts' : 1, 'sponsor_popularity' : 1, 'special_trait' : 18}
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
cornicopiaWeapons = numpy.array([hatchet1, hatchet2, knife1, knife2, knife3, knife4, knife5, knife6, knife7, knife8, bow_and_arrows1, bow_and_arrows2, spear1, spear2, darts1, darts2, sling1, sling2, sword1, sword2, sword3])
cornicopiaWeaponsCatalog = numpy.array(cornicopiaWeapons)
cornicopiaItems = numpy.array(['medkit', 'medkit', 'medkit', 'largeRation', 'largeRation', 'smallRation', 'smallRation', 'smallRation', 'smallRation', 'smallRation', 'tarp', 'tarp', 'tarp', 'tarp', 'tarp', 'tarp', 'backpackLarge', 'backpackSmall', 'backpackSmall'])
for player in players:
    if players.get(player).get('smarts') < 6 or players.get(player).get('strength') > 7:
        bloodbath.append(player)
        bloodbathBattle = numpy.array(bloodbath)
random.shuffle(cornicopiaWeapons)
random.shuffle(bloodbathBattle)
for player in bloodbathBattle:
    if players.get(player).get('strength') > 9:
        cornicopiaWeapons[0].owner = player
        print(f"{player} grabs a {cornicopiaWeapons[0].name}")
        cornicopiaWeapons = numpy.delete(cornicopiaWeapons, 0)
    if players.get(player).get('strength') > 7:
        cornicopiaWeapons[0].owner = player
        print(f"{player} grabs a {cornicopiaWeapons[0].name}")
        cornicopiaWeapons = numpy.delete(cornicopiaWeapons, 0)
    if players.get(player).get('strength') < 7 and players.get(player).get('strength') > 3:
        cornicopiaWeapons[0].owner = player
        print(f"{player} grabs a {cornicopiaWeapons[0].name} this should be interesting...")
        cornicopiaWeapons = numpy.delete(cornicopiaWeapons, 0)
    if players.get(player).get('strength') < 3:
        bloodbathFatalitieLocation = numpy.where(player)
        bloodbathFatalitieString = str(bloodbathFatalitieLocation)
        bloodbathFatalitieCleaned1 = bloodbathFatalitieString.replace("(array([", "")
        bloodbathFatalitieCleaned2 = bloodbathFatalitieCleaned1.replace("]),)", "")
        #print(bloodbathFatalitieCleaned2)
        bloodbathFatalitie = int(bloodbathFatalitieCleaned2)
        if bloodbathFatalitie < len(bloodbathBattle) - 1:
            for weaponTool in cornicopiaWeaponsCatalog:
                if weaponTool.owner == bloodbathBattle[bloodbathFatalitie + 1]:
                    how = weaponTool.name
                else:
                    how = "with their fists"
            print(f"{player} was killed by {bloodbathBattle[bloodbathFatalitie + 1]} with {how}")
        else:
            print(f"{player} was killed by {bloodbathBattle[bloodbathFatalitie - 2]}")
