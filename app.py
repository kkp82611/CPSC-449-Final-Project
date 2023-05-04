#change this to the flask
from typing import Optional
from fastapi import Body, FastAPI, Path
from pydantic import BaseModel
from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient("mongodb://localhost:27017")
db = client["book"]
book_list = db["book_list"]
app = FastAPI()


book =  {
         "title": "book_title",
         "author": "book_author",
         "description": "book_description",
         "price": 20.99,
         "stock": 5
    }


class Book(BaseModel):
    title: str
    author: str
    description: str
    price: float
    stock: int

class UpdateBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None


@app.get('/')
def index():
	return {'name': 'First Data'}

#● GET /books: Retrieves a list of all books in the store
@app.get('/books')
def get_book():
    new_book_list = book_list.find({},{"_id": 0})
    result_book = []
    for x in new_book_list:
        result_book.append(x)
    print(result_book)

    return result_book

#● GET /books/{book_id}: Retrieves a specific book by ID
@app.get('/books/{book_id}')
def get_one_book(book_id: str):
    mybook = book_list.find_one({"_id": ObjectId(book_id)},{"_id": 0})
    return mybook

#● POST /books: Adds a new book to the store
@app.post('/books')
def add_book(add_book: Book):
    book_list.insert_one(add_book.__dict__)
    return "book added" 
     
#● PUT /books/{book_id}: Updates an existing book by ID
@app.put("/books/{book_id}")
def update(book_id: str, update_book: UpdateBook):
    newvalues = {"$set" : update_book.__dict__}
    book_list.update_one({'_id': ObjectId(book_id)}, newvalues)
    return "book updated"

#● DELETE /books/{book_id}: Deletes a book from the store by ID
@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    book_list.delete_one({'_id': ObjectId(book_id)})
    return "book deleted"
     
#● GET /search?title={}&author={}&min_price={}&max_price={}: Searches for books by title, author, and price range
@app.get("/search")
def search_book(title: str = {"$exists":True}, author: str =  {"$exists":True}, min_price: float = 0, max_prie: float = 999999999):
    print(author)

    result_book = book_list.find({"title": title, "author": author, "price":{"$gte":min_price,"$lt":max_prie}},{"_id": 0})
    cbook = []
    for x in result_book:
        cbook.append(x)
    return cbook



