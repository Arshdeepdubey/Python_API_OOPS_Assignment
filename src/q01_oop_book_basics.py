# TODO:
# 1) Define class Book with attributes: title, author, price
# 2) Implement method get_details(self) -> "Title: <...>, Author: <...>, Price: <...>"
# 3) Create 3 Book instances and print their details using get_details()

class Book:
    def __init__(self, title, author, price):
        self.title=title
        self.author=author
        self.price=price

    def get_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

if __name__ == "__main__":
    book_1=Book('Friends, Family and the Big Terrible Thing', 'Mathew Perry', '265 rupees')
    book_2=Book('Steve Jobs', 'Walter Isaacson', '445 rupees')
    book_3=Book('The Tempest', 'William Shakespeare', '650 rupees')
    book_1.get_details()
    book_2.get_details()
    book_3.get_details()