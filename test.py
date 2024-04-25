URL = "https://discord.com/api/webhooks/1233164999178981456/sNNzdaM9oGp7R1rb1o1u2amaxgzR-OiznzohVukd_U6zrouaFDIRJd7BTbYfuPj3nW9I"

import requests
import time
from bs4 import BeautifulSoup

mod_list = ["3120415400", "3103482941", "3220925251", "3221688644", "3222017090", "3112614550", "3197306614",
            "3224786979", "3225207245", "3228532387", "3229219637", "3230010267", "3229606298", "3229348152"]


def send_discord_message(webhook_url, message):
    data = {"content": message}
    response = requests.post(webhook_url, json=data)
    return response.status_code


def check_for_mod_updates():
    # URL of the page

    for mod in mod_list:
        time.sleep(5)
        url = "https://steamcommunity.com/sharedfiles/filedetails/?id=" + mod

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
                send_discord_message(URL, date_element.text.strip())
            else:
                print("Date element not found.")
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)


check_for_mod_updates()

#
