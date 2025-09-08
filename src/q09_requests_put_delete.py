# TODO:
# 1) PUT https://jsonplaceholder.typicode.com/posts/1 with some updated JSON payload.
# 2) DELETE https://jsonplaceholder.typicode.com/posts/1
# 3) Print both status codes. Print JSON for PUT response.

import requests
import json

def do_put():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = {
        "title": "Updated Title",
        "body": "This post has been updated",
        "userId": 1
    }
    response = requests.put(url, json=data)
    print("PUT Request:")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Updated post:")
        print(json.dumps(response.json(), indent=2))
    return response.status_code == 200

def do_delete():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url)
    print("\nDELETE Request:")
    print(f"Status Code: {response.status_code}")
    return response.status_code == 200

def verify_deletion():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    print("\nVerifying deletion:")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 404:
        print("Post was successfully deleted")
    else:
        print("Post still exists")

if __name__ == "__main__":
    print("PUT status:", do_put())
    print("DELETE status:", do_delete())