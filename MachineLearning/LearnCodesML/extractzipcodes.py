import requests
from bs4 import BeautifulSoup

# URL to fetch ZIP codes from
url = 'https://projects.tampabay.com/projects/data/coronavirus/en/zipcode'

# Make a request to the webpage
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <a> tags with rel="prefetch" that contain ZIP codes in their href attribute
zip_code_links = soup.find_all('a', rel="prefetch", href=True)

# Extract ZIP codes from the href attribute or the text
zip_codes = [link.text.strip() for link in zip_code_links if link['href'].startswith('en/zipcode/')]

# Print the list of ZIP codes
print(zip_codes)

# Optionally, save this list to a file
with open('zip_codes.txt', 'w') as file:
    for zip_code in zip_codes:
        file.write(f"{zip_code}\n")
