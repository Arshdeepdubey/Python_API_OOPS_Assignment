# TODO:
# Create a robust fetch_url function that handles different status codes appropriately
# Use the status classifier from q10

from q10_http_status_classifier import classify_status_code
import requests
from urllib.parse import urlparse

class URLFetchError(Exception):
    def __init__(self, status_code, category, description):
        self.status_code = status_code
        self.category = category
        self.description = description
        super().__init__(f"{status_code} ({category}): {description}")

def fetch_url(url, max_retries=3):
    """
    Fetch URL with proper status code handling and retries
    """
    if not url.startswith(('http://', 'https://')):
        raise ValueError("URL must start with http:// or https://")
    
    if not bool(urlparse(url).netloc):
        raise ValueError("Invalid URL format")
    
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url, timeout=10)
            category, description = classify_status_code(response.status_code)
            
            if 200 <= response.status_code < 300:
                return response.json()
            elif response.status_code >= 500:
                attempt += 1
                if attempt < max_retries:
                    print(f"Attempt {attempt} failed, retrying...")
                    continue
            
            raise URLFetchError(response.status_code, category, description)
        
        except requests.RequestException as e:
            raise URLFetchError(0, "Network Error", str(e))
    
    raise URLFetchError(response.status_code, category, "Max retries exceeded")

def main():
    # Test with different URLs
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",  # Should work
        "https://jsonplaceholder.typicode.com/nonexistent",  # 404
        "https://httpstat.us/500",  # 500 error
        "invalid-url"  # Invalid URL
    ]
    
    for url in urls:
        print(f"\nTrying URL: {url}")
        try:
            result = fetch_url(url)
            print("Success!")
            print(f"Result: {result}")
        except URLFetchError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Invalid URL: {e}")

if __name__ == "__main__":
    main()
# Implement fetch_data(url: str) that:
# - GETs the URL
# - Prints "Success" if 200
# - Prints "Client Error" if 400–499
# - Prints "Server Error" if 500–599
# - Else prints "Unexpected status code: <code>"
# - Handles exceptions (ConnectionError, Timeout) and prints a message.
# Test with:
#  - https://jsonplaceholder.typicode.com/posts/1  (should be 200)
#  - https://jsonplaceholder.typicode.com/invalid  (404)
#  - an obviously wrong URL like http://does-not-exist.example (should except)

import requests

def fetch_data(url: str) -> None:
    # your code here
    pass

if __name__ == "__main__":
    # tests
    pass
