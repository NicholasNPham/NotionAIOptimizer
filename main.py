from notion_client import Client

# File Imports
from workschedule import reversedDictSchedule
from key import *

# Initialize client with your token
notion = Client(auth=secret)

# Your database ID
database_id = pageID

# Query the database
response = notion.databases.query(database_id=database_id)

# Print the results, Uncomment to print
for page in response['results']:
    properties = page['properties']
    # print(properties)

# Results gets all the database rows in a dictionary
results = notion.databases.query(database_id=pageID)
# The pages variable stores the list of page objects
pages = results['results']

# Zip called to pair elements from the two dictionaries that turned into lists
for page, (key, value) in zip(pages, reversedDictSchedule.items()):
    rowID = page['id']
    # Format dictionary of shift date as text in NOTION API SCHEMA
    textProperty = {"Shift": {"title": [{"text": {"content": key}}]}}
    # Format dictionary of hours scheduled in NOTION API SCHEMA
    hourProperty = {"Hour": {"number": value[1]}}
    # Format dictionary of shift time in NOTION API SCHEMA
    if value[0] == "No Shift Scheduled":
        dateProperty = {"Date": {"date": None}}
    else:
        dateProperty = {"Date": {"date": {"start": value[0][0], "end": value[0][1]}}}

    # Code Below will be to create a variable containing text,hour,date property to update 3 in 1 per 1 in 14 days

    # Try Block to update database "Work Schedule Database"
    try:
        response = notion.pages.update(page_id=rowID, properties=dateProperty)
        print("page updated", response)
    except Exception as e:
        print(e)