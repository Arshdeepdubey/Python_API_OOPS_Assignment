# TODO:
# Implement classify_status(code: int) -> str
# Returns: "Success" (2xx), "Created" (201 only), "Client Error" (4xx), "Server Error" (5xx), else "Other"
# Print classification for: 200, 201, 400, 401, 403, 404, 500, 502, 503

def classify_status(code: int) -> str:
    """
    Classify HTTP status code into its category
    Returns tuple of (category_name, description)
    """
    if not isinstance(code, int):
        raise ValueError("Status code must be an integer")

    if 100 <= code <= 199:
        return "Informational", "Request received, continuing process"
    elif 200 <= code <= 299:
        return "Success", "Request was successfully received and processed"
    elif 300 <= code <= 399:
        return "Redirection", "Further action needs to be taken"
    elif 400 <= code <= 499:
        return "Client Error", "Request contains bad syntax or cannot be fulfilled"
    elif 500 <= code <= 599:
        return "Server Error", "Server failed to fulfill a valid request"
    else:
        return "Unknown", "Invalid HTTP status code"

if __name__ == "__main__":
    codes = [200, 201, 400, 401, 403, 404, 500, 502, 503]
    for c in codes:
        print(c, "->", classify_status(c))