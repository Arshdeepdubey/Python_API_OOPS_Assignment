# Combined OOP exercise demonstrating various OOP concepts
# Including: encapsulation, class methods, magic methods, composition

class Price:
    def __init__(self, value: float, currency: str = "INR"):
        if not isinstance(value, (int, float)):
            raise TypeError("Price value must be a number")
        if value < 0:
            raise ValueError("Price cannot be negative")
        if not isinstance(currency, str) or len(currency.strip()) == 0:
            raise ValueError("Currency must be a non-empty string")
            
        self._value = float(value)
        self._currency = currency.upper().strip()
    
    def __str__(self) -> str:
        return f"{self._currency} {self._value:.2f}"
    
    def __repr__(self) -> str:
        return f"Price({self._value}, '{self._currency}')"
    
    @property
    def value(self) -> float:
        return self._value
    
    @property
    def currency(self) -> str:
        return self._currency

class Book:
    def __init__(self, title: str, author: str, price: Price):
        if not isinstance(title, str) or len(title.strip()) == 0:
            raise ValueError("Title must be a non-empty string")
        if not isinstance(author, str) or len(author.strip()) == 0:
            raise ValueError("Author must be a non-empty string")
        if not isinstance(price, Price):
            raise TypeError("Price must be a Price object")
            
        self.title = title.strip()
        self.author = author.strip()
        self.price = price
    
    def __str__(self) -> str:
        return f"{self.title} by {self.author} - {self.price}"
    
    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}', {repr(self.price)})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title.lower() == other.title.lower() and 
                self.author.lower() == other.author.lower())
    
    @classmethod
    def from_dict(cls, d: dict) -> 'Book':
        try:
            price = Price(float(d['price']), d.get('currency', 'INR'))
            return cls(d['title'], d['author'], price)
        except (KeyError, ValueError) as e:
            raise ValueError(f"Invalid dictionary format: {e}")

class Inventory:
    def __init__(self):
        self._books = []
    
    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Can only add Book objects")
        self._books.append(book)
    
    def remove_book(self, title: str, author: str) -> bool:
        book_to_remove = Book(title, author, Price(0))  # Price doesn't matter for comparison
        try:
            self._books.remove(book_to_remove)
            return True
        except ValueError:
            return False
    
    def find_by_author(self, author: str) -> list[Book]:
        return [book for book in self._books 
                if book.author.lower() == author.lower()]
    
    def __len__(self) -> int:
        return len(self._books)
    
    def __iter__(self):
        return iter(self._books)

if __name__ == "__main__":
    # Create books from dictionaries
    books_data = [
        {"title": "The Psychology of Money", "author": "Morgan Housel", "price": 499},
        {"title": "Atomic Habits", "author": "James Clear", "price": 699},
        {"title": "Deep Work", "author": "Cal Newport", "price": 599}
    ]
    
    # Initialize inventory
    inventory = Inventory()
    
    # Add books to inventory
    print("Adding books to inventory:")
    for data in books_data:
        book = Book.from_dict(data)
        inventory.add_book(book)
        print(f"Added: {book}")
    
    # Print total books
    print(f"\nTotal books in inventory: {len(inventory)}")
    
    # Remove a book
    removed = inventory.remove_book("Atomic Habits", "James Clear")
    print(f"\nRemoved 'Atomic Habits': {removed}")
    print(f"Books now in inventory: {len(inventory)}")
    
    # Find books by author
    author = "Morgan Housel"
    print(f"\nBooks by {author}:")
    for book in inventory.find_by_author(author):
        print(f"- {book}")
    
    # Demonstrate iteration
    print("\nAll books in inventory:")
    for book in inventory:
        print(f"- {book}")
