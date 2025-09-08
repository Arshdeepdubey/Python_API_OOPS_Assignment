# Build a tiny CLI:
# Usage:
#   python q12_cli_http_client.py GET https://jsonplaceholder.typicode.com/posts/1
#   python q12_cli_http_client.py POST https://jsonplaceholder.typicode.com/posts '{"title":"x","body":"y","userId":1}'
# Requirements:
# - Accept method in {GET, POST, PUT, DELETE}
# - Optional JSON body for POST/PUT (as a raw JSON string argument)
# - Print status code and JSON (if any) or text.
# - Handle invalid method and JSON errors gracefully.

import sys
import requests
import json
from urllib.parse import urlparse

def validate_url(url):
    """Validate URL format"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def make_request(method, url, data=None):
    """Make HTTP request and return response"""
    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            json=data if data else None
        )
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

def print_response(response):
    """Pretty print response"""
    if not response:
        return
    
    print("\nResponse:")
    print(f"Status: {response.status_code}")
    print("\nHeaders:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
    
    print("\nBody:")
    try:
        print(json.dumps(response.json(), indent=2))
    except:
        print(response.text)

def main(argv):
    # Check arguments
    if len(argv) < 2:
        print("Usage: python cli_http_client.py METHOD URL [JSON_BODY]")
        print("Methods: GET, POST, PUT, DELETE")
        sys.exit(1)
    
    # Parse arguments
    method = argv[0].upper()
    url = argv[1]
    data = None
    
    # Validate method
    if method not in {'GET', 'POST', 'PUT', 'DELETE'}:
        print(f"Error: Invalid method '{method}'. Use GET, POST, PUT, or DELETE")
        sys.exit(1)
    
    # Validate URL
    if not validate_url(url):
        print(f"Error: Invalid URL format '{url}'")
        sys.exit(1)
    
    # Parse JSON body if provided for POST/PUT
    if len(argv) > 2 and method in {'POST', 'PUT'}:
        try:
            data = json.loads(argv[2])
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format: {e}")
            sys.exit(1)
    
    # Make request and print response
    try:
        response = make_request(method, url, data=data)
        if response:
            print_response(response)
        else:
            print("Error: Request failed")
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])