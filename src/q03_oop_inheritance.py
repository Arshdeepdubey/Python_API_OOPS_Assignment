# TODO:
# Create subclass EBook(Book) with extra attribute file_size (MB: float|int)
# Override get_details to include file_size, e.g., "... , File Size: 2.5MB"
# Instantiate EBook and print details + discounted price.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = float(price)
    
    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}"
    
    def get_price_after_discount(self, discount=0.1):
        if 0 <= discount <= 1:
            return self.price * (1 - discount)
        raise ValueError("Discount must be between 0 and 1")

class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = float(file_size)
    
    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, File Size: {self.file_size:.1f}MB"

if __name__ == "__main__":
    digital_book = EBook(
        title="Programming",
        author="John Smith",
        price=29.50,
        file_size=2.9
    )
    
    # Print book details
    print("Book Details:")
    print(digital_book.get_details())
    
    # Calculate and print discounted price (15% discount)
    discount = 0.15
    discounted_price = digital_book.get_price_after_discount(discount)
    print(f"\nPrice after {discount*100}% discount: ${discounted_price:.2f}")
