import requests
import re

def detect_xss(url):
    response = requests.get(url)
    if response.status_code == 200:
        body = response.text
        if re.search(r"<\s*script", body) or re.search(r"on\w+=", body):
            if re.search(r"<\s*script\s*alert\(", body):
                return "Reflected XSS with alert() function"
            elif re.search(r"<\s*img\s*src\s*=.*javascript:", body):
                return "Reflected XSS with JavaScript injection in image source"
            elif re.search(r"<\s*a\s*href\s*=.*javascript:", body):
                return "Reflected XSS with JavaScript injection in link"
            elif re.search(r"document\.cookie", body):
                return "Stored XSS with access to cookie"
            else:
                return "Possible XSS vulnerability"
    return "No XSS vulnerability detected"

# Get user input for URL
url = input("Enter a URL to check for XSS vulnerabilities: ")

# Call the detect_xss function with the user input
result = detect_xss(url)

# Print the result
print(result)
