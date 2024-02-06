import requests
from bs4 import BeautifulSoup
import csv

# ziplist = ['33613', '33612', '33611', '33610', '33609', '33608', '33607', '33606', '33605', '33604', '33603', '33602', '33601']
# ziplist = ['33510', '33511', '33527', '33534', '33547', '33548', '33549', '33556', '33558', '33559', '33563', '33565',
#         '33566', '33567', '33569', '33570', '33572', '33573', '33578', '33579', '33584', '33592', '33594', '33596',
#         '33598', '33602', '33603', '33604', '33605', '33606', '33607', '33609', '33610', '33611', '33612', '33613',
#         '33614', '33615', '33616', '33617', '33618', '33619', '33624', '33625', '33626', '33629', '33634', '33635',
#         '33637', '33647']
with open('zip_codes.txt', 'r') as file:
    ziplist = [line.strip() for line in file]
print("ziplist is created")
# Open a CSV file to write
with open('unemployment_rates.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row with % sign in the column name
    writer.writerow(['Zip Code', 'Unemployment Rate (%)'])
    
    for zp in ziplist:
        # URL of the page to scrape
        url = f'https://zipatlas.com/us/fl/zip-code-{zp}.htm'

        # Send a GET request to the URL
        response = requests.get(url)

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Initialize variable to hold the unemployment rate
        unemployment_rate = "Unavailable"

        # Find all divs and iterate to find the one with "UNEMPLOYMENT RATE"
        for div in soup.find_all('div'):
            if div.text == "UNEMPLOYMENT RATE":
                unemployment_rate = div.find_previous_sibling('div').text
                # Remove the % sign from the unemployment rate
                unemployment_rate = unemployment_rate.replace('%', '').strip()
                break

        # Write the ZIP code and its unemployment rate (without % sign) to the CSV file
        writer.writerow([zp, unemployment_rate])
