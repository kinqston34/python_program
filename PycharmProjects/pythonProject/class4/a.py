import csv
birth_year = []
with open(r'C:\Users\User\Desktop\voteData\2010村里長\elcand.csv',encoding='UTF-8') as f:
    # while True:          # way1
    #     s = f.readline()
    #     if not s:
    #         break
    #     data = s.split(",")
    #     birth_year.append(int(data[9]))
    data = csv.reader(f)        #way2
    for x in data:
        birth_year += [int(x[9])]
print(birth_year)
ages = [99-x for x in birth_year]
mu = sum(ages)/len(ages)
varience_list = [(x-mu)**2 for x in ages]
#varience = sum(varience_list)/len(varience_list)
varience = sum(varience_list)/(len(varience_list)-1)
print(sum(ages)/len(ages))
import math
print(math.sqrt(varience))