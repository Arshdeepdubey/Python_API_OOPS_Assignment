# TODO:
# 1) GET https://jsonplaceholder.typicode.com/posts/1
# 2) Print the response JSON and specifically print the "title" field.

import requests

def main():
    # Make GET request to the API
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        
        # Print full response
        print("Full Response:")
        print(f"User ID: {data['userId']}")
        print(f"ID: {data['id']}")
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
        
        # Print specifically the title
        print("\nTitle field:")
        print(data['title'])
    else:
        print(f"Error: {response.status_code}")
        print(f"Message: {response.text}")

if __name__ == "__main__":
    main()
