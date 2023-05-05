import numpy
import csv
print("THE HUNGER GAMES")

print("enter the values below 1 to 10")
print("enter by puting name then stringth then friendlyness then smarts then sponsor popularity separated by commas. when you are done enter 'May The Odds Be Ever In Your Favor' capitalized just like that")

player = ""


with open('players.csv', 'r') as players:
    reader = csv.reader(players)
for row in reader:
    print(row)    
