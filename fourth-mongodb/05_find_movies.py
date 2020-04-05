from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie = db.movies.find_one({'title':'어벤져스: 엔드게임'})
print (target_movie['star'])

db.people.update_many({'star': "9.38"},{'$set': {'star': "0.00"}})
# print(db.people)