import csv
birth_year = []
with open(r'C:\Users\User\Desktop\voteData\2010村里長\elcand.csv',encoding='UTF-8') as f:
    data = csv.reader(f)  # way2
    for x in data:
        birth_year += [int(x[9])]
ages = [99 - x for x in birth_year]
import statistics as stat
print('avg',stat.mean(ages))
print('population,母體標準差',stat.pstdev(ages))
print('sample,樣本標準差',stat.stdev(ages))
print(stat.median(ages),stat.mode(ages))