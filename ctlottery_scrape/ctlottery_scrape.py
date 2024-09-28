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
"""
import ee
import geemap

# Authenticate and initialize the Earth Engine API
ee.Authenticate()
ee.Initialize()

# Define the region of interest (Puerto Rico)
puerto_rico = ee.Geometry.Polygon(
    [[[-67.945404, 17.88328],
      [-67.945404, 18.515683],
      [-65.220703, 18.515683],
      [-65.220703, 17.88328]]]
)

# Filter the Landsat 8 image collection for Puerto Rico
landsat8 = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR') \
    .filterBounds(puerto_rico) \
    .filterDate('2023-01-01', '2023-12-31') \
    .filterMetadata('CLOUD_COVER', 'less_than', 20)

# Select the median image
median_image = landsat8.median().clip(puerto_rico)

# Define visualization parameters
vis_params = {
    'bands': ['B4', 'B3', 'B2'],
    'min': 0,
    'max': 3000,
    'gamma': 1.4
}

# Create a map and add the median image layer
Map = geemap.Map(center=[18.2, -66.5], zoom=8)
Map.addLayer(median_image, vis_params, 'Landsat 8 Median Image')
Map.addLayer(puerto_rico, {}, 'Puerto Rico')
Map.addLayerControl()
Map
"""

"""
//Javascript equivalent
// Define the geometry for Puerto Rico
var puerto_rico = ee.Geometry.Polygon([
  [[-67.945404, 17.88328],
   [-67.945404, 18.515683],
   [-65.220703, 18.515683],
   [-65.220703, 17.88328]]
]);

// Load the Landsat 8 ImageCollection
var landsat8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_SR')
  .filterBounds(puerto_rico)
  .filterDate('2023-01-01', '2023-12-31')
  .filterMetadata('CLOUD_COVER', 'less_than', 20);

// Compute the median image and clip it to Puerto Rico
var median_image = landsat8.median().clip(puerto_rico);

// Visualization parameters
var vis_params = {
  bands: ['B4', 'B3', 'B2'],
  min: 0,
  max: 3000,
  gamma: 1.4
};

// Add the median image to the map
Map.centerObject(puerto_rico, 8);
Map.addLayer(median_image, vis_params, 'Landsat 8 Median Image');
Map.addLayer(puerto_rico, {}, 'Puerto Rico');
Map.addLayerControl();
"""