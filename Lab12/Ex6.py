# Retrieve Hawaii mortgage rates from hicentral.com and extract the rate table

import ssl
import requests
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
print(f"Fetching: {url}\n")

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers, verify=False)

soup = BeautifulSoup(response.text, 'lxml')

# The page has one table with Lender, Term/Type, Interest Rate, % Points, % APR
table = soup.find('table')

# Print the header row
headers_row = [th.get_text(strip=True) for th in table.find('thead').find_all('th')]
print(f"{'  |  '.join(headers_row)}")
print('-' * 70)

# Banks use rowspan so their name only appears in the first of their rows.
# We track current_bank and reuse it for subsequent rows until a new bank appears.
current_bank = ''

for row in table.find('tbody').find_all('tr'):
    cells = row.find_all('td')

    if len(cells) == 5:
        # First row for this bank — bank name is in the first cell
        current_bank = cells[0].get_text(separator=' ', strip=True)
        term, rate, points, apr = [c.get_text(strip=True) for c in cells[1:]]
    elif len(cells) == 4:
        # Continuation row — bank name carried over from rowspan above
        term, rate, points, apr = [c.get_text(strip=True) for c in cells]
    else:
        continue

    print(f"{current_bank:<35} {term:<18} Rate: {rate}%  Points: {points}  APR: {apr}%")
