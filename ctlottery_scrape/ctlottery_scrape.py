import requests
from bs4 import BeautifulSoup
import csv

# URL of the page to scrape
url = 'https://www.ctlottery.org/ScratchGamesTable'

# Send a GET request to the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the scratch games data
    table = soup.find('table', {'id': 'gvScratchGames'})

    # Extract the headers
    headers = [header.text for header in table.find_all('th')]

    # Extract the rows
    rows = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cells = row.find_all('td')
        row_data = [cell.text.strip() for cell in cells]
        rows.append(row_data)

    # Define the file path
    file_path = r'C:\Users\jsoto\OneDrive\Documents\My Tableau Repository\Datasources\Lottery\ctlottery.csv'

    # Write the data to a CSV file
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write the headers
        writer.writerows(rows)  # Write the data rows

    print(f"Data successfully written to {file_path}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
