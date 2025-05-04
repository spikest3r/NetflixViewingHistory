import csv

result = []

f = open("viewinghistory.txt",'w')

total = 0

print("To get viewing history go to https://www.netflix.com/settings/viewing-history and press 'Download all'")
fileName = input("CSV file name (leave blank for default NetflixViewingHistory.csv): ")
if len(fileName) == 0:
    fileName = "NetflixViewingHistory.csv"
with open(fileName,'r') as file:
    csvreader = csv.reader(file)
    fields = next(csvreader)
    for row in csvreader:
        data = row[0].split(":")
        if not data[0] in result:
            result.append(data[0])
            print(data[0])
            f.write(data[0] + '\n')
            total += 1

print("Total: ",total)


