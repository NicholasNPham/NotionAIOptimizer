from notion_client import Client

# File Imports
from workschedule import reversedDictSchedule
from key import *
from datetime import datetime

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
    # Give name variable a string to open,close and etc.
    if value[0] != 'No Shift Scheduled':
            startTime = value[0][0][:22] + value[0][1][-2:]
            endTime = value[0][1][:22] + value[0][1][-2:]
            dt = datetime.strptime(startTime, "%Y-%m-%dT%H:%M:%S%z")
            dt2 = datetime.strptime(endTime, "%Y-%m-%dT%H:%M:%S%z")
            if dt.strftime("%H:%M") == "05:30":
                name = "Opening Shift"
            elif dt2.strftime("%H:%M") == "21:00":
                name = "Closing Shift"
            elif dt.strftime("%H:%M") == "9:00":
                name = "Curbside Shift"
            else:
                name = "Misc Shift"
    else:
        name = "No Shift Scheduled"
    textProperty = {"title": [{"text": {"content": name}}]}
    # Format dictionary of hours scheduled in NOTION API SCHEMA
    hourProperty = {"number": value[1]}
    # Format dictionary of shift time in NOTION API SCHEMA
    if value[0] == "No Shift Scheduled":
        dateProperty = {"date": None}
    else:
        dateProperty = {"date": {"start": value[0][0], "end": value[0][1]}}
    # Code Below will be to create a variable containing text,hour,date property to update 3 in 1 per 1 in 14 days
    propertyDict = {"Hour": hourProperty, "Date": dateProperty, "Shift": textProperty}

    # Try Block to update database "Work Schedule Database"
    try:
        response = notion.pages.update(page_id=rowID, properties=propertyDict)
        print("page updated", response)
    except Exception as e:
        print(e)