# import requests
# from bs4 import BeautifulSoup

# # URL of the page
# url = 'https://projects.tampabay.com/projects/data/coronavirus/en/zipcode/32003'

# # Send a GET request
# response = requests.get(url)

# # Parse the HTML content
# soup = BeautifulSoup(response.text, 'html.parser')

# # Now, you need to find the specific data you are interested in. 
# # This is just an example to get you started.
# # For instance, if you're looking for a table:
# tables = soup.find_all('table')
# # Assuming your data is in the first table
# data_rows = tables[0].find_all('tr')  # if the data is in a table row

# for row in data_rows:
#     data = row.find_all('td')  # Assuming the details are in 'td' tags
#     print([td.text for td in data])  # Print each cell in the row

import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import os
# URL of the CSV file
# Initialize an empty list to store ZIP codes
zip_codes = []

# Open the file and read each line
with open('zip_codes.txt', 'r') as file:
    for line in file:
        # Strip newline and whitespace and add to the list
        zip_codes.append(line.strip())

print(len(zip_codes))
zipcode=["33854"]
for zp in zip_codes:
    csv_url = 'https://tbt-covid-public.s3.amazonaws.com/zip_cases/app-data/zip/'+str(zp)+'.csv'

# Use pandas to read the CSV file directly from the URL

    data = pd.read_csv(csv_url,parse_dates=['date'])
    path='../../Data/data/zipcodes/'
    filename=str(zp)+'.csv'
    data.to_csv(os.path.join(path,filename),index=False)
# Display the first few rows of the dataframe
#     plt.plot(data['date'], data['new_cases_per_cap_rolling_weekly_mean'])
# plt.legend(zip_codes[:10])

# You can now work with the 'data' dataframe to analyze the time series data
# For example, to plot the number of cases over time, you can use:
# data.plot(x='Date', y='Cases')

# print(data.tail())
# ax=plt.gca()
# ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
# plt.gcf().autofmt_xdate()
# plt.show()