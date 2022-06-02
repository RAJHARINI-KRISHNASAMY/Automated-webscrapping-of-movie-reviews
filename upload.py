from pymongo import MongoClient
import pandas as pd
df = pd.read_csv('movie.csv')
df.reset_index(inplace=True)
data = df.to_dict('records')
db = MongoClient("")
x = db["movieReviewDatabase"]["Pirates of the Caribbean"].insert_many(data)
