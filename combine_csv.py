import csv
import glob

files = glob.glob("shared/*.csv")

all_games = []

for f in files:
    with open(f, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[1] != "turns":
                all_games.append( (int(row[1]), row[2]) )

output = open("combined.csv", "w")
output.write("turns,succeeded?\n")
for game in all_games:
    output.write("%d,%s\n" % game)

output.close()
