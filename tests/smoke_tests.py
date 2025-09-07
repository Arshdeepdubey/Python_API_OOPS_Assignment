"""
Smoke tests for Python API and OOP Assignment
Run with: python -m unittest tests/smoke_tests.py
"""

import unittest
import sys
import os
from pathlib import Path

# Add src directory to Python path
root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

def run_file(filename):
    """Run a Python file and check if it executes without errors"""
    file_path = root_dir / "src" / filename
    if not file_path.exists():
        return False, f"File not found: {filename}"
    
    try:
        with open(file_path, 'r') as f:
            exec(f.read(), {})
        return True, "OK"
    except Exception as e:
        return False, str(e)

class TestFileExecution(unittest.TestCase):
    """Test if all Python files can be executed without errors"""
    
    def test_basic_oop(self):
        """Test q01-q05: OOP concepts"""
        files = [
            "q01_oop_book_basics.py",
            "q02_oop_encapsulation.py",
            "q03_oop_inheritance.py",
            "q04_oop_polymorphism.py",
            "q05_oop_all_in_one.py"
        ]
        for file in files:
            with self.subTest(file=file):
                success, message = run_file(file)
                self.assertTrue(success, f"Error in {file}: {message}")
    
    def test_http_requests(self):
        """Test q06-q09: HTTP requests"""
        files = [
            "q06_requests_get.py",
            "q07_requests_get_params.py",
            "q08_requests_post.py",
            "q09_requests_put_delete.py"
        ]
        for file in files:
            with self.subTest(file=file):
                success, message = run_file(file)
                self.assertTrue(success, f"Error in {file}: {message}")
    
    def test_http_utils(self):
        """Test q10-q12: HTTP utilities"""
        files = [
            "q10_http_status_classifier.py",
            "q11_fetch_with_status_handling.py",
            "q12_cli_http_client.py"
        ]
        for file in files:
            with self.subTest(file=file):
                success, message = run_file(file)
                self.assertTrue(success, f"Error in {file}: {message}")

class TestOOPImplementation(unittest.TestCase):
    """Test specific OOP implementations"""
    
    def test_book_basics(self):
        """Test basic Book class implementation"""
        from src.q01_oop_book_basics import Book
        book = Book("Test Book", "Test Author", "499")
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.price, "499")
    
    def test_encapsulation(self):
        """Test encapsulation with discount property"""
        from src.q02_oop_encapsulation import Book
        book = Book(100)
        book.get_discount = 0.2
        self.assertEqual(book.get_discount, 0.2)
        self.assertEqual(book.get_price_after_discount(), 80.0)
    
    def test_inheritance(self):
        """Test inheritance with EBook class"""
        from src.q03_oop_inheritance import Book, EBook
        ebook = EBook("Digital Book", "Test Author", 29.99, 2.5)
        self.assertTrue(isinstance(ebook, Book))
        self.assertIn("2.5MB", ebook.get_details())
    class TestOOPBasics(unittest.TestCase):
    """Test basic OOP concepts from q01"""
    
    def setUp(self):
        self.book = BasicBook("Python Programming", "John Smith", "499")
    
    def test_book_attributes(self):
        self.assertEqual(self.book.title, "Python Programming")
        self.assertEqual(self.book.author, "John Smith")
        self.assertEqual(self.book.price, "499")
    
    def test_get_details(self):
        details = self.book.get_details()
        self.assertIn("Python Programming", details)
        self.assertIn("John Smith", details)
        self.assertIn("499", details)

class TestEncapsulation(unittest.TestCase):
    """Test encapsulation concepts from q02"""
    
    def setUp(self):
        self.book = EncapsulatedBook(100)
    
    def test_discount_property(self):
        self.book.get_discount = 0.2
        self.assertEqual(self.book.get_discount, 0.2)
    
    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            self.book.get_discount = 1.5  # Should be between 0 and 1
    
    def test_discounted_price(self):
        self.book.get_discount = 0.2
        self.assertEqual(self.book.get_price_after_discount(), 80.0)

class TestInheritance(unittest.TestCase):
    """Test inheritance concepts from q03"""
    
    def setUp(self):
        self.ebook = EBook("Digital Python", "Jane Doe", 29.99, 2.5)
    
    def test_inheritance_chain(self):
        self.assertTrue(isinstance(self.ebook, EBook))
        self.assertTrue(isinstance(self.ebook, ParentBook))
    
    def test_attributes(self):
        self.assertEqual(self.ebook.title, "Digital Python")
        self.assertEqual(self.ebook.file_size, 2.5)
    
    def test_method_override(self):
        details = self.ebook.get_details()
        self.assertIn("2.5MB", details)

class TestPolymorphism(unittest.TestCase):
    """Test polymorphism concepts from q04"""
    
    def setUp(self):
        self.book = PolyBook("Regular Book", "Author One", "299")
        self.ebook = PolyEBook("Digital Book", "Author Two", "199", "PDF")
        self.items = [self.book, self.ebook]
    
    def test_polymorphic_behavior(self):
        for item in self.items:
            details = item.get_details()
            self.assertIn(item.title, details)
            self.assertIn(item.author, details)

class TestHTTPUtils(unittest.TestCase):
    """Test HTTP utility functions"""
    
    def test_status_classification(self):
        test_cases = [
            (200, "Success"),
            (404, "Client Error"),
            (500, "Server Error"),
            (301, "Redirection"),
            (102, "Informational")
        ]
        for code, expected in test_cases:
            category, _ = classify_status_code(code)
            self.assertEqual(category, expected)
    
    @patch('requests.get')
    def test_url_fetch(self, mock_get):
        # Mock successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response
        
        result = fetch_url("https://api.example.com/test")
        self.assertEqual(result["data"], "test")
    
    def test_invalid_url(self):
        with self.assertRaises(ValueError):
            fetch_url("invalid-url")

if __name__ == '__main__':
    unittest.main()
]

for f in FILES:
    print(f"Running {f} ...")
    p = subprocess.run([sys.executable, str(ROOT / f)], capture_output=True, text=True)
    print(p.stdout)
    if p.returncode != 0:
        print(p.stderr)
        raise SystemExit(f"Failed: {f}")
print("Done.")
