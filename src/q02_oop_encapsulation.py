# TODO:
# Extend Book with a "private" discount attribute _discount (default=0.1)
# Add getter/setter for discount with validation (0.0 <= discount <= 0.9)
# Add method get_price_after_discount() -> price*(1-discount)
# Demonstrate setting discount via setter and print the discounted price.

class Book:
    def __init__(self, price, discount=0.1):
        self.price=price
        self._discount=discount

    @property
    def get_discount(self):
        return self._discount

    @get_discount.setter
    def get_discount(self, value):
        if 0.1 <= value <= 0.9:
            self._discount = value
        else:
            raise ValueError("Discount must be between 0.1 and 0.9")

    def get_price_after_discount(self):
        return self.price * (1 - self._discount)

if __name__ == "__main__":
    price = float(input('enter the price money: '))
    book_1 = Book(price)
    discount = float(input('enter the valid discount for price (0.1-0.9): '))
    book_1.get_discount = discount  # Use property assignment, not method call
    print(f"Original price: ${book_1.price}")
    print(f"Discount: {book_1.get_discount}%")
    print(f"Final price: ${book_1.get_price_after_discount()}")
