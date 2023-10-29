"""
Purpose: Convert Excel files to GeoJson
Note: Also need to download ``openpyxl``
"""
import json
import pandas as pd
import string

can_province_abbrev = {
  'Alberta': 'AB',
  'British Columbia': 'BC',
  'Manitoba': 'MB',
  'New Brunswick': 'NB',
  'Newfoundland And Labrador': 'NL',
  'Northwest Territories': 'NT',
  'Nova Scotia': 'NS',
  'Nunavut': 'NU',
  'Ontario': 'ON',
  'Prince Edward Island': 'PE',
  'Quebec': 'QC',
  'Saskatchewan': 'SK',
  'Yukon': 'YT'
}

can_province_names = {
  'AB': 'Alberta',
  'BC': 'British Columbia',
  'MB': 'Manitoba',
  'NB': 'New Brunswick',
  'NL': 'Newfoundland And Labrador',
  'NS': 'Nova Scotia',
  'NT': 'Northwest Territories',
  'NU': 'Nunavut',
  'ON': 'Ontario',
  'PE': 'Prince Edward Island',
  'QC': 'Quebec',
  'SK': 'Saskatchewan',
  'YT': 'Yukon'
}

# Load the CSV data into a Pandas DataFrame
data = pd.read_excel('cafes.xlsx')

# Create a new DataFrame to store the GeoJSON features
features = []

# Loop through the rows of the CSV data and create a GeoJSON feature for each point
for index, row in data.iterrows():
  feature = {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [row['longitude'], row['latitude']]
    },
    "properties": {
      "name": row['name'],
      "address": row['address'],
      "province": string.capwords(row['province']),
      "province_code": can_province_abbrev[string.capwords(row['province'])]
    }
  }
  features.append(feature)

# Create a GeoJSON FeatureCollection to store all the features
geojson_data = {
  "type": "FeatureCollection",
  "features": features
}

# Convert the GeoJSON data to a string
geojson_str = json.dumps(geojson_data, indent=2)

# Save the GeoJSON string to a file
with open('../public/static/json/cafes.geojson', 'w', encoding='utf-8') as f:
  f.write(geojson_str)
