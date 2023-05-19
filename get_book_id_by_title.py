import requests

# Specify the book title for which you want to retrieve the ID
title = "Harry Potter"

# Send the GET request to retrieve the book ID
response = requests.get(f"http://localhost:8000/books/{title}")

# Check the response status code
if response.status_code == 200:
    response_json = response.json()
    if "book_id" in response_json:
        book_id = response_json["book_id"]
        print(f"Book ID of {title}:", book_id)
    else:
        print("Book not found")
else:
    print("Failed to retrieve the book ID")
