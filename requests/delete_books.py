import requests

# Specify the book ID you want to delete
book_id = "6467295b90b5ca6b91970c19"

# Send the DELETE request to delete the book
response = requests.delete(f"http://localhost:8000/books/{book_id}")

# Check the response status code
if response.status_code == 200:
    print("Book deleted successfully.")
else:
    print("Failed to delete the book.")
