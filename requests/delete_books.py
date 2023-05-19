import requests

# Specify the book ID you want to delete
book_id = "6467308bbcfc269cea0833c8"

# Send the DELETE request to delete the book
response = requests.delete(f"http://localhost:8000/books/{book_id}")

# Check the response status code
if response.status_code == 200:
    print("Book deleted successfully.")
else:
    print("Failed to delete the book.")
