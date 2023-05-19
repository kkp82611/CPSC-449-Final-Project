import requests

# Define the book details
new_book = {
    "title": "Harry Potter",
    "author": "J.K. Rowling",
    "description": "A book about a wizard boy going to a wizard school.",
    "price": 10.00,
    "stock": 15
}

# Send the POST request to add the book
response = requests.post("http://localhost:8000/books", json=new_book)

# Check the response status code
if response.status_code == 200:
    print("Book added successfully.")
else:
    print("Failed to add the book.")
