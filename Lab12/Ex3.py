# Use BeautifulSoup to parse the ITM people page and extract faculty names

import ssl
import urllib.request
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://shidler.hawaii.edu/itm/people"
print(f"Opening URL: {url}")

html = urllib.request.urlopen(url).read()

# BeautifulSoup parses the raw HTML into a navigable tree object.
# This is useful because we can search, filter, and extract specific tags
# without having to manually parse HTML strings.
soup = BeautifulSoup(html, 'lxml')

# Print the first few lines of the prettified HTML
print("\n--- First 5 lines of prettified HTML ---")
for i, line in enumerate(soup.prettify().splitlines()):
    if i >= 5:
        break
    print(line)

# Each person is inside an <article> tag with class "node-faculty"
# Their name is inside <h2 class="title"> > <a> > <span>
people = []
for article in soup.find_all('article', class_='node-faculty'):
    name_tag = article.find('h2', class_='title')
    if name_tag:
        name = name_tag.get_text(strip=True)
        people.append(name)

print(f"\nFound {len(people)} people:\n")
for person in people:
    print(f"  {person}")
