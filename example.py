import getpass
import json
import pandas
import requests
import sys

from emsapi import emsapi

url = "https://ems.efoqa.com/api/"
user = input('Enter your EFOQA username: ')
pwd = getpass.getpass(prompt = 'Enter your EFOQA password: ')

# Set some api connection variables.
client = emsapi.create(user, pwd, url)
client.config.connection.timeout = 400
client.config.retry_policy.retries = 2

# Print the systems the user has access to in order to demonstrate the API.
systems = client.ems_system.get_ems_systems()
sysList = list(map(lambda system: [system.id, system.name, system.description], systems))
df = pandas.DataFrame(sysList, columns=['id', 'name', 'description'])

print("You have access to the following systems:")
print(df.head())

# Print the offsets for a parameter of a flight.

# Baro-corrected altitude
altitudeId = "H4sIAAAAAAAEAG2Q0QuCMBDG34P+B/HdbZVUiApBPQT2kgi9rrn0YM7aZvbnN5JVUvdwfHD34/vu4iPXrbjTs+D7kksDF+DKezRC6ggSvzbmGmHc9z3qF6hVFZ4TMsOnQ5azmjc0AKkNlYz7A/Mm9GusUUkNZa00ijLj+BCTFd6UgApF/XQ68bx4SMHVvkyd1GjX6KytgFER46+FEZBfObOZ2db6eBBJEIlvVGfz4P+LhYRbZ29NyVCzgJD1MgitDIhrrj6+P/h04obj36VPLpuOeVIBAAA="

# EMS7 - the demo system.
emsId = client.find_ems_system_id('ems7-app')

# A flight that is known to exist
flightId = 190

# Pull out altitude with 100 samples through the file.
query = {
    "select": [
        {
            "analyticId": altitudeId
        }
    ],
    "size": 100
}

# Execute the API call.
altitude = client.analytic.get_query_results(emsId, flightId, query)
print(altitude.offsets)

# Find top 20 flight ids with valid takeoff and landing
query = {
  "select": [
    {
      "fieldId": "[-hub-][field][[[ems-core][entity-type][foqa-flights]][[ems-core][base-field][flight.uid]]]",
      "aggregate": "none"
    },
    {
      "fieldId": "[-hub-][field][[[ems-core][entity-type][foqa-flights]][[ems-core][base-field][flight.exist-takeoff]]]",
      "aggregate": "none"
    }
  ],
  "filter": {
      "operator": "and",
      "args": [
          {
              "type": "filter",
              "value": {
                  "operator": "isTrue",
                  "args": [
                      {
                          "type": "field",
                          "value": "[-hub-][field][[[ems-core][entity-type][foqa-flights]][[ems-core][base-field][flight.exist-takeoff]]]"
                      }
                  ]
              }
          },
          {
              "type": "filter",
              "value": {
                  "operator": "isTrue",
                  "args": [
                      {
                          "type": "field",
                          "value": "[-hub-][field][[[ems-core][entity-type][foqa-flights]][[ems-core][base-field][flight.exist-landing]]]"
                      }
                  ]
              }
          }
      ]
  },
  "groupBy": [],
  "orderBy": [],
  "distinct": True,
  "top": 20,
  "format": "display"
}

result = client.database.get_query_results(emsId, '[ems-core][entity-type][foqa-flights]', query)
pd = pandas.DataFrame(result.rows, columns=['Flight Record', 'Takeoff Exists'])
print(pd)

# Run the same query using the async query route and include more flights
query['top'] = 800

async_result = client.database.start_async_query(emsId, '[ems-core][entity-type][foqa-flights]', query)
if client.is_error(async_result):
    error = client.get_error_message(async_result)
    raise ValueError(error)

async_query_id = async_result.id
start_index = 0
batch_size = 100
while True:
    end_index = start_index + (batch_size - 1)
    result = client.database.read_async_query(emsId, '[ems-core][entity-type][foqa-flights]', async_query_id, start_index, end_index)
    if client.is_error(result):
        break # Some kind of error occurred
    
    if result.rows and len(result.rows) > 0:
        for row in result.rows:
            print(row)
    
    if not result.has_more_rows:
        break
    
    start_index = end_index + 1
    
client.database.stop_async_query(emsId, '[ems-core][entity-type][foqa-flights]', async_query_id)