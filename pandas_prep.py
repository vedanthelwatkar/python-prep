import pandas as pd

df = pd.read_csv('./archive/apple.csv')

df.head()
df.tail()
df.describe()
df.filter(['year', 'month'], axis=1)

print('pandas series ==> ', type(df['year']))
print('pandas dataframe ==>', type(df[['year', 'month']]))

print("rename ==> ")
df.rename(columns={'sale_id':'id'})

series = df['year']
print('indexing in series ==> ', series[9])

series[9] = 2026
print('replacing in series ==> ', series[9])

print('series.iloc ==> ', series.iloc[5:10])
print('series loc ==> ', series.loc[9])

print('df.iloc ==> ', df.iloc[[3,5], [8,9]])
print('df.loc ==> ', df.loc[[3,7],['year','month']])

df.isna()
print('df.isna ==> ', df.isna().sum())

isna_check = df[df['storage'].isna()]
print('isna_check: ', isna_check)

print("tail before ==> " ,df.tail())
print("fill na func ==> ")
df = df.fillna(0)
print("tail after ==> " ,df.tail())

print("update using loc ==>")
df.loc[9, 'year'] = 2026

print("update using iloc ==> ")
df.iloc[8,2] = 2026
print("bool filtering ==> ", df[df['year']==2026])


