# TODO:
# 1) GET https://jsonplaceholder.typicode.com/comments with params: postId=1
# 2) Print the length of results and print first 2 items (pretty as JSON).

import requests
import json

def main():
    # Define the URL and parameters
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {
        "postId": 1
    }
    
    # Make GET request with parameters
    response = requests.get(url, params=params)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        comments = response.json()
        
        # Print the total number of comments
        print(f"Total comments found: {len(comments)}")
        
        # Print first 2 comments with pretty formatting
        print("\nFirst 2 comments:")
        for comment in comments[:2]:
            # Use json.dumps with indent for pretty printing
            print(json.dumps(comment, indent=2))
            print("-" * 50)  # Separator between comments
    else:
        print(f"Error: {response.status_code}")
        print(f"Message: {response.text}")

if __name__ == "__main__":
    main()
