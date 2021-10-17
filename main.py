import numpy as np
import pandas as pd

#creating a series by passing a list of values, panda creates a default and changeable integer index
series = pd.Series(["cake", "cookies", "icecream"])

#customize indices
series = pd.Series(["cake", "cookies", "icecream"], index=["I like:", "I love:", "I'm addicted to:"])

num_series = pd.Series([9, 42, 7]) #, index=["First Number", "Second Number", "Third Number"])

#mathematical operations on series - not possible this way with python lists
#print(num_series["Third Number"], num_series*2)

num_series2 = pd.Series([1, 2, 3])

#print(num_series+num_series2)

#To create a dataframe, first implement a dictionary, than pass it to pandas

data = {"Numbers": [7,5,3],
        "Letters": ["S","W","T"]}

dataframe = pd.DataFrame(data)

#now one can use shape and len(), shape shows how much colums and rows, len shows how much rows

#print(dataframe.shape, len(dataframe))

#to get an overview over the dataframe, pandas provides the info() function

#print(dataframe.info())

#you can choose the data you want by specifying the key, or by specifying the index using loc

#print(dataframe["Letters"], dataframe.loc[1])

#indices can also be customized and called by loc

dataframe = pd.DataFrame(data, index=["Zero", "One", "Two"])

#print(dataframe.loc["One"])

#iloc makes it possible to call the index independently from renaming

#print(dataframe.iloc[1])

#loc and iloc always call the column and the row values, to get a single value, use at
#one needs to pass index and rowname to get the value

#print(dataframe.at["Zero", "Numbers"])

#to use actual indices, use iat

print(dataframe.iat[0, 0])
