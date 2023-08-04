from pymongo import MongoClient


client = MongoClient('mongodb://logger_read_only:E3Fj2o9F@85.105.50.16:2717/?authSource=admin&readPreference=primary&directConnection=true&ssl=false')

db = client.logger_db

col = db.iq_horizon_mac_filtered_office


for x in col.find({},{ "_id": 1, "last_update": 1}):
  print(x)

"""
{'_id': '64ba533177c9abe4647c778e', 'las_update': '2023,8,4,8,58,26,823000'}

"""