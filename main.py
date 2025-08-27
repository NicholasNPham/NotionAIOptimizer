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

testDictionary = {
    "2025-08-25": ["No Shift Scheduled", 0],
    "2025-08-26": [['2025-08-26T14:00:00-04:00', '2025-08-26T21:00:00-04:00'], 7.0]
}

# Results gets all the database rows in a dictionary
results = notion.databases.query(database_id=pageID)
# The pages variable stores the list of page objects
pages = results['results']

# Zip called to pair elements from the two dictionaries that turned into lists
for page, (key, value) in zip(pages, reversedDictSchedule.items()):
    rowID = page['id']
    textProperty = {"Shift": {"title": [{"text": {"content": key}}]}}

    # Try Block to update database "Work Schedule Database"
    try:
        response = notion.pages.update(page_id=rowID, properties=textProperty)
        print("page updated", response)
    except Exception as e:
        print(e)

# This is CODE HELL VVVV WILL BE CHANGED

    # if value[0] == "No Shift Scheduled":
    #     startTimeProperties, endTimeProperties = None, None
    #     hourProperties = value[1]
    # else:
    #     startTimeProperties = value[0][0]
    #     endTimeProperties = value[0][1]
    #     hourProperties = value[1]

    # if startTimeProperties == None and endTimeProperties == None:
    #     dateProperty = {"date": None}
    # else:
    #     dateProperty = {"date": {"start": startTimeProperties, "end": endTimeProperties}}
    # hourProperty = {"number": hourProperties}
    #
    # properties = {"Shift": textProperty, "Start Time": dateProperty, "Hours": hourProperty}


