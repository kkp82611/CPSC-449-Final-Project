from flask import Flask, render_template
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/book"
mongo = PyMongo(app)

online_users = mongo.db.users.find({"online": True})



#GET /books: Retrieves a list of all books in the store
@app.route("/books", methods=['GET'])
def books():
    list_book = []
    return list_book

#GET /books/{book_id}: Retrieves a specific book by ID
@app.route('/books/<path:bookid>', methods=['GET'])
def books_id(bookid):
    list_book = []
    return list_book

#POST /books: Adds a new book to the store
@app.route('/books' , methods=['POST'])
def add_book():
 
    return "add book success"

#PUT /books/{book_id}: Updates an existing book by ID
@app.route('/books/<path:bookid>', methods=['PUT'])
def update_book(bookid):
    return "update success"

#DELETE /books/{book_id}: Deletes a book from the store by ID
@app.route('/books/<path:bookid>' , method = ['DELETE'])
def delete_book(bookid):
    return "delete success"

#GET /search?title={}&author={}&min_price={}&max_price={}: Searches for books by title, author, and price range[]

@app.route('search?title={}&author={}&min_price={}&max_price={}', method= ['GET'])
def search_book():
    book = []
    return book
