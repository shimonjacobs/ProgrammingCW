from generate_adresses import generate_addresses as gen
import csv

points=[10, 100, 500]

for n in points:
    x=gen(n, 100)
    with open(f"{n}_points.csv", "w") as file:
        spamwriter=csv.writer(file, delimiter=' ')
        for i in x:
            spamwriter.writerow(i)

