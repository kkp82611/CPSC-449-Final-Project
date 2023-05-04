from typing import Optional
from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient("mongodb://localhost:27017")
db = client["book"]
book_list = db["book_list"]

result = db.create_collection("book_list", validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'additionalProperties': True,
            'required': ['title', 'author', "description", "price", "stock"],
            'properties': {
                'title': {
                    'bsonType': 'string',
                    'description': 'title should be string'
                },
                'author': {
                    'bsonType': 'string',
                    'description': 'author should be string'
                },
                'description': {
                    'bsonType': 'string',
                    'description': 'description should be string'
                },
                'price': {
                    'bsonType': 'double',
                    'description': 'price should be float'
                },
                'stock': {
                    'bsonType': 'int',
                    'description': 'stock should be int'
                }
            }
        }
    }
    
)




#book =  {
#         "title": "book_title",
#         "author": "book_author",
#         "description": "book_description",
#         "price": 20.99,
#         "stock": 5
#    }

#create index by the title which is usually way to check
book_list.create_index("title")
#create index by price that if searxh by price
book_list.create_index("price")
#create index by stock if search by stock
book_list.create_index("stock")


