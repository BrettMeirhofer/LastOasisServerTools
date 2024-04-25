import requests
from bs4 import BeautifulSoup

# URL of the page
url = "https://steamcommunity.com/sharedfiles/filedetails/?id=3120415400"

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element containing the update date
    # This example assumes the date is stored in a specific element; you might need to adjust the selector.
    date_element = soup.find('div', class_='detailsStatsContainerRight')

    if date_element:
        print("Last updated date:", date_element.text.strip())
    else:
        print("Date element not found.")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)