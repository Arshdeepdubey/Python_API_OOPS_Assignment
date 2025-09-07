# TODO:
# Create a command-line HTTP client that supports:
# - GET, POST, PUT, DELETE methods
# - Custom headers
# - Request body for POST/PUT
# - Pretty printed response

import argparse
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

def parse_headers(headers):
    """Parse header string into dictionary"""
    if not headers:
        return {}
    try:
        return dict(h.split(':') for h in headers.split(','))
    except:
        raise ValueError("Headers must be in format 'key1:value1,key2:value2'")

def make_request(method, url, headers=None, data=None):
    """Make HTTP request and return response"""
    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
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

def main():
    parser = argparse.ArgumentParser(description="Command-line HTTP client")
    parser.add_argument('method', choices=['get', 'post', 'put', 'delete'],
                      help='HTTP method')
    parser.add_argument('url', help='Target URL')
    parser.add_argument('--headers', help='Headers in format "key1:value1,key2:value2"')
    parser.add_argument('--data', help='JSON data for POST/PUT requests')
    
    args = parser.parse_args()
    
    # Validate URL
    if not validate_url(args.url):
        print("Error: Invalid URL format")
        return
    
    # Parse headers
    try:
        headers = parse_headers(args.headers)
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    # Parse data if provided
    data = None
    if args.data:
        try:
            data = json.loads(args.data)
        except json.JSONDecodeError:
            print("Error: Invalid JSON data")
            return
    
    # Make request
    response = make_request(args.method, args.url, headers, data)
    if response:
        print_response(response)

if __name__ == "__main__":
    main()
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
import json
import requests

def main(argv):
    # your code here
    pass

if __name__ == "__main__":
    main(sys.argv[1:])
