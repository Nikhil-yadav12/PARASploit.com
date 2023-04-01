import re

def detect_xss(url):
    pattern = re.compile(r"<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>|<alert\b[^<]*(?:(?!<\/alert>)<[^<]*)*<\/alert>", re.IGNORECASE)
    match = pattern.search(url)
    
    if match:
        print("Possible XSS attack detected!")
    else:
        print("No XSS attack detected.")

# Prompt the user to enter a URL:
url_input = input("Enter a URL to check for XSS: ")

# Call the detect_xss() function with the user's input:
detect_xss(url_input)
