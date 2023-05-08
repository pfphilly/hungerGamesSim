import csv
print("THE HUNGER GAMES")

print("enter the values below 1 to 10")
print("enter by puting name then stringth then friendlyness then smarts then sponsor popularity separated by commas. when you are done enter 'May The Odds Be Ever In Your Favor' capitalized just like that")


players = []

with open('players.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        players.append(row)
print(players)
