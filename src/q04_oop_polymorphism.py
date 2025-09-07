# TODO:
# Implement print_details(obj) that works for both Book and EBook (duck typing)
# Create a list [Book(...), EBook(...), ...] and iterate to print details.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = float(price)
    
    def get_details(self):
        return {
            "type": "Physical Book",
            "title": self.title,
            "author": self.author,
            "price": f"${self.price:.2f}"
        }

class EBook(Book):
    def __init__(self, title, author, price, format_type):
        super().__init__(title, author, price)
        self.format_type = format_type
    
    def get_details(self):
        details = super().get_details()
        details["type"] = "Digital Book"
        details["format"] = self.format_type
        return details

def print_details(obj):
    """Print details of any book type object that has get_details() method"""
    try:
        details = obj.get_details()
        print("\n" + "="*50)
        print(f"Type: {details['type']}")
        print(f"Title: {details['title']}")
        print(f"Author: {details['author']}")
        print(f"Price: {details['price']}")
        if 'format' in details:
            print(f"Format: {details['format']}")
        print("="*50)
    except AttributeError:
        print("Error: Object doesn't have required get_details() method")

if __name__ == "__main__":
    # Create instances of both types
    physical_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 14.99)
    digital_book1 = EBook("Python Crash Course", "Eric Matthes", 29.99, "PDF")
    digital_book2 = EBook("Clean Code", "Robert Martin", 24.99, "EPUB")
    
    # Create a list of books
    books = [physical_book, digital_book1, digital_book2]
    
    # Demonstrate polymorphism by iterating through the list
    print("Demonstrating Polymorphism with Different Book Types:")
    for book in books:
        print_details(book)
    
    # Demonstrate duck typing - print_details works with any object that has get_details()
    print("\nTrying with invalid object:")
    try:
        print_details("Not a book object")
    except AttributeError as e:
        print(f"Error: {e}")
