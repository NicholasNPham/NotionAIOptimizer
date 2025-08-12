from notion_client import Client
from key import *

# Initialize client with your token
notion = Client(auth=secret)

# Your database ID
database_id = dbID

# Query the database
response = notion.databases.query(database_id=database_id)

# Print the results
for page in response['results']:
    properties = page['properties']
    print(properties)  # you can format this based on your database properties