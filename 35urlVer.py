import re

def check_valid_url(url):
    """
    Checks if a given URL is valid or not using regex.
    """
    # Define the regex pattern for a valid URL
    pattern = r"^(http|https)://[a-zA-Z0-9]+([\-\.]{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,5}(:[0-9]{1,5})?(\/.*)?$"

    # Use the search() function to find a match for the pattern
    match = re.search(pattern, url)
    
    # Return True if there is a match, otherwise False
    if match:
        return True
    else:
        return False

# Test the function with some examples
url1 = "https://www.google.com/"
url2 = "http://www.example.com/index.html"
url3 = "www.invalid-url.com"
url4 = "ftp://ftp.example.com"

print(check_valid_url(url1))
print(check_valid_url(url2)) 
print(check_valid_url(url3)) 
print(check_valid_url(url4))
