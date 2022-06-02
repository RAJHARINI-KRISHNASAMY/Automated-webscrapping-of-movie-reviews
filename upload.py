from pymongo import MongoClient
import pandas as pd
df = pd.read_csv('movie.csv')
df.reset_index(inplace=True)
data = df.to_dict('records')
db = MongoClient("mongodb://BDAT1004:Password@cluster0-shard-00-00.gzlae.mongodb.net:27017,cluster0-shard-00-01.gzlae.mongodb.net:27017,cluster0-shard-00-02.gzlae.mongodb.net:27017/movieReviewDatabase?ssl=true&replicaSet=atlas-qnmzak-shard-0&authSource=admin&retryWrites=true&w=majority")
x = db["movieReviewDatabase"]["Pirates of the Caribbean"].insert_many(data)
