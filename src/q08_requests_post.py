# TODO:
# 1) POST https://jsonplaceholder.typicode.com/posts
#    body: {"title": "OOPs Assignment", "body": "Learning Python requests", "userId": 101}
# 2) Print status_code and response JSON (expect an "id" returned by the fake API).

import requests
import json

def main():
    # Define URL and request body
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "OOPs Assignment",
        "body": "Learning Python requests",
        "userId": 101
    }
    
    # Make POST request
    response = requests.post(url, json=data)
    
    # Print status code
    print(f"Status Code: {response.status_code}")
    
    # Print response JSON
    if response.status_code in [200, 201]:
        result = response.json()
        print("\nResponse:")
        print(json.dumps(result, indent=2))
        print(f"\nCreated post with ID: {result['id']}")
    else:
        print(f"Error: {response.text}")

if __name__ == "__main__":
    main()
