from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['scrapper']
Users = db['facebook_users']
Users.create_index([("facebook_id")], unique=True)

def insert_user(user): 
  try:
    new_user = Users.insert_one(user)
    print(new_user.id)
  except Exception as e:
    print("Duplicate key or mongo error: ")