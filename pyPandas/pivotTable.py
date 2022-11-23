import pandas as pd

df = pd.read_excel('fooddata.xlsx')
df = df[[ 'Calories','Category','Food Item']]
df = df.sort_values(by = ['Calories'],ascending= False)

print(df)

#trying to get the total number of items per category
#print(df.groupby('Category').value_counts()) 

pivot = df.pivot_table(index= 'Category',  values='Calories', aggfunc= 'sum')

print(pivot)

##pivot.to_excel('pivot.xlsx', 'totalCalories', startrow = 0)

