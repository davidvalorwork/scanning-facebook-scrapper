from facebook_scraper import get_profile
from utils.write_csv import write_csv
from models.pymongo import Users, insert_user
from models.models import User

res = get_profile('David.EV.DesarrolloWeb', cookies='cookies.txt', friends=True)

if('Friend_count' in res):
  user = User.serialization(res)
  insert_user(user)

  if('Friends' in res):
    friends = res['Friends']
    print(len(friends))
    print(list(friends[0]))
    i = 0
    for friend in friends:
        i = i + 1
        print(str(i) + ' ' + str(friend['name']) + ' '+ str(friend['id']))
        users_replica = Users.find_one({"facebook_id": str(friend['id'])})
        if(users_replica is None):
          print("Getting profile of "+ friend['name'])
          res = get_profile(str(friend['id']), cookies='cookies.txt', friends=True)
          user = User.serialization(res)
          insert_user(user)