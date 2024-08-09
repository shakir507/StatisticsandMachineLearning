from bs4 import BeautifulSoup
import os
from googlesearch import search

def get_first_google_link(query):
    try:
        for j in search(query, num_results=1):
            return j
    except Exception as e:
        print(f"Error fetching link for {query}: {e}")
        return "#"

path = '../../Data/ReferencesXML/'

# Read the EndNote file
with open(os.path.join(path, 'CreateReferences.xml'), 'r') as file:
    endnote_xml = file.read()

# Parse the XML using BeautifulSoup
soup = BeautifulSoup(endnote_xml, 'xml')

# Create a new HTML file to store the references
with open(os.path.join(path, 'references.html'), 'w') as html_file:
    html_file.write('<html><body><ol>')  # Changed from <ul> to <ol> for enumeration

    # Iterate over each reference in the EndNote file
    for record in soup.find_all('record'):
        title = record.find('title').text if record.find('title') else "No Title"
        url = get_first_google_link(title)

        # Write the reference as a linked item in the HTML file, adding a <br> tag for spacing
        html_file.write(f'<li><a href="{url}">{title}</a></li><br>')  # Added <br> for spacing

    html_file.write('</ol></body></html>')
