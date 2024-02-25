import requests
from bs4 import BeautifulSoup
ziplist=['33613','33612','33611','33610','33609','33608','33607','33606','33605','33604','33603','33602','33601']

for zp in ziplist:
    # URL of the page to scrape
    url = f'https://zipatlas.com/us/fl/zip-code-{zp}.htm'

    # Send a GET request to the URL
    response = requests.get(url)
    print(response.text)
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize variable to hold the unemployment rate
    unemployment_rate = "Unavailable"

    # Find all divs and iterate to find the one with "UNEMPLOYMENT RATE"
    for div in soup.find_all('div'):
        if div.text == "UNEMPLOYMENT RATE":
            unemployment_rate = div.find_previous_sibling('div').text
            break

    print(f"Unemployment Rate for {zp}: {unemployment_rate}")
# # URL of the page to scrape
# url = 'https://zipatlas.com/us/fl/zip-code-33613.htm'

# # Send a GET request to the URL
# response = requests.get(url)

# # Parse the HTML content of the page using BeautifulSoup
# soup = BeautifulSoup(response.text, 'html.parser')

# # Initialize variable to hold the unemployment rate
# unemployment_rate = "Unavailable"

# # Find all divs and iterate to find the one with "UNEMPLOYMENT RATE"
# for div in soup.find_all('div'):
#     if div.text == "UNEMPLOYMENT RATE":
#         unemployment_rate = div.find_previous_sibling('div').text
#         break

# print(f"Unemployment Rate: {unemployment_rate}")
