import pandas as pd

data = {
    'apples': [3, 2, 0, 1], 
    'oranges': [0, 3, 7, 2]
}

purchases = pd.DataFrame(data, index=['Yulita','Awan','Robert','Joko'])
print(purchases)
print(purchases.loc['Yulita'])
# write to csv
purchases.to_csv('new_purchases.csv')

# load from csv
movies = pd.read_csv('IMDB-Movie-Data.csv',index_col='Title')
#show data
print(movies.head(10))
#show last data
print(movies.tail(10))
#show info
print(movies.info())
#show row and column
print(movies.shape())