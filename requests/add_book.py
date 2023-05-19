import requests

# Define the book details
new_book = {
    "title": "Crime and Punishment",
    "author": "Fyodor Dostoevsky",
    "description": "A man commits a crime he didn't realize the consequences for.",
    "price": 8.00,
    "stock": 46
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