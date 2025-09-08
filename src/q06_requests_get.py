# TODO:
# 1) GET https://jsonplaceholder.typicode.com/posts/1
# 2) Print the response JSON and specifically print the "title" field.

import requests

def main():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        print(f"User ID: {data['userId']}")
        print(f"ID: {data['id']}")
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
        print(data['title'])
    else:
        print(f"Error: {response.status_code}")
        print(f"Message: {response.text}")

if __name__ == "__main__":
    main()
