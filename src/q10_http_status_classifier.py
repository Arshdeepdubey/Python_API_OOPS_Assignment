# TODO:
# Create a function to classify HTTP status codes into their categories
# 1xx: Informational
# 2xx: Success
# 3xx: Redirection
# 4xx: Client Error
# 5xx: Server Error

def classify_status_code(status_code):
    """
    Classify HTTP status code into its category
    Returns tuple of (category_name, description)
    """
    if not isinstance(status_code, int):
        raise ValueError("Status code must be an integer")
    
    if 100 <= status_code <= 199:
        return "Informational", "Request received, continuing process"
    elif 200 <= status_code <= 299:
        return "Success", "Request was successfully received and processed"
    elif 300 <= status_code <= 399:
        return "Redirection", "Further action needs to be taken"
    elif 400 <= status_code <= 499:
        return "Client Error", "Request contains bad syntax or cannot be fulfilled"
    elif 500 <= status_code <= 599:
        return "Server Error", "Server failed to fulfill a valid request"
    else:
        return "Unknown", "Invalid HTTP status code"

def main():
    # Test with different status codes
    test_codes = [200, 404, 500, 302, 100]
    
    for code in test_codes:
        category, description = classify_status_code(code)
        print(f"\nStatus Code: {code}")
        print(f"Category: {category}")
        print(f"Description: {description}")

if __name__ == "__main__":
    main()
# Implement classify_status(code: int) -> str
# Returns: "Success" (2xx), "Created" (201 only), "Client Error" (4xx), "Server Error" (5xx), else "Other"
# Print classification for: 200, 201, 400, 401, 403, 404, 500, 502, 503

def classify_status(code: int) -> str:
    # your code here
    pass

if __name__ == "__main__":
    codes = [200, 201, 400, 401, 403, 404, 500, 502, 503]
    for c in codes:
        print(c, "->", classify_status(c))
