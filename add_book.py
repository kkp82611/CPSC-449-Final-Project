import requests

# Define the book details
new_book = {
    "title": "The Lord of the Rings",
    "author": "J. R. R. Tolkien",
    "description": "The Lord of the Rings is an epic high-fantasy novel by English author and scholar.",
    "price": 7.50,
    "stock": 33
}

# Send the POST request to add the book
response = requests.post("http://localhost:8000/books", json=new_book)

# Check the response status code
if response.status_code == 200:
    response_json = response.json()
    new_book_id = response_json["book_id"]
    print("New book added with ID:", new_book_id)
else:
    print("Failed to add the book")