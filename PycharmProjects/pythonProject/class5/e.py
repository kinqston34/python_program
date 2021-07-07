import pandas as pd
#DataFrame: 加強版的dic
df = pd.read_csv(r'C:\Users\User\Desktop\elcand.csv',names = ['c0','c1','c2','c3','c4','c5','c6','c7','c8','birthYear','c10','c11','c12','c13','elected','c15'])
#print(df)
#print(df['birthYear'])
df['age'] = 99 - df['birthYear']
print(df['age'].describe())
print(df['age'].describe()['mean'])