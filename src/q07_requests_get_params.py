# TODO:
# 1) GET https://jsonplaceholder.typicode.com/comments with params: postId=1
# 2) Print the length of results and print first 2 items (pretty as JSON).

import requests
import json

def main():
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {
        "postId": 1
    }
    response = requests.get(url, params=params)  
    if response.status_code == 200:
        comments = response.json()
        
        print(f"Total comments found: {len(comments)}")
        print("\nFirst 2 comments:")
        for comment in comments[:2]:
            print(json.dumps(comment, indent=2))
            print("#" * 50)
    else:
        print(f"Error: {response.status_code}")
        print(f"Message: {response.text}")

if __name__ == "__main__":
    main()
