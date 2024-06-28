from urllib.request import urlopen
from bs4 import BeautifulSoup

with urlopen("http://www.google.com") as caner:
    body = caner.read().decode('utf-8')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(body, 'html.parser')

# Print the well-formatted HTML content
print(soup.prettify())
