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

from q10_http_status_classifier import classify_status
import requests
from urllib.parse import urlparse

class URLFetchError(Exception):
    def __init__(self, status_code, category, description):
        self.status_code = status_code
        self.category = category
        self.description = description
        super().__init__(f"{status_code} ({category}): {description}")

def fetch_data(url: str) -> None:
    """
    Fetch URL with proper status code handling and retries
    """
    if not url.startswith(('http://', 'https://')):
        raise ValueError("URL must start with http:// or https://")
    
    if not bool(urlparse(url).netloc):
        raise ValueError("Invalid URL format")
    
    max_retries = 3
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url, timeout=10)
            category, description = classify_status(response.status_code)
            
            if 200 <= response.status_code < 300:
                print("Success")
            elif 400 <= response.status_code < 500:
                print("Client Error")
            elif 500 <= response.status_code < 600:
                print("Server Error")
            else:
                print(f"Unexpected status code: {response.status_code}")

            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            attempt += 1
            if attempt >= max_retries:
                raise URLFetchError(0, "Network Error", str(e))

    raise URLFetchError(0, "Network Error", "Max retries exceeded")

def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/nonexistent",
        "https://httpstat.us/500",
        "invalid-url"
    ]

    for url in urls:
        print(f"\nTrying URL: {url}")
        try:
            result = fetch_data(url)
            print("Success!")
            print(f"Result: {result}")
        except URLFetchError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Invalid URL: {e}")

if __name__ == "__main__":
    main()
