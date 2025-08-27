from notion_client import Client

# File Imports
from workschedule import dictSchedule
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

# Finding Valid Page ID
results = notion.databases.query(database_id=pageID)
for page in results['results']:
    validPageID = page['id']
    print(validPageID)

for key, value in dictSchedule.items():

    if value[0] == "No Shift Scheduled":
        shiftProperties = key
        startTimeProperties, endTimeProperties = None, None
        hourProperties = value[1]
    else:
        shiftProperties = key
        startTimeProperties = value[0][0]
        endTimeProperties = value[0][1]
        hourProperties = value[1]

    textProperty = [{"text": {"content": shiftProperties}}]
    if startTimeProperties == None and endTimeProperties == None:
        dateProperty = {"date": None}
    else:
        dateProperty = {"date": {"start": startTimeProperties, "end": endTimeProperties}}
    hourProperty = {"number": hourProperties}

    properties = {
        "Shift": textProperty,
        "Start Time": dateProperty,
        "Hours": hourProperty
    }

    # Try Block to update database "Work Schedule Database"
    try:
        response = notion.pages.update(page_id=validPageID, properties=dateProperty)
        print("page updated", response)
    except Exception as e:
        print(f'error updating page {e}')


"""

    Research:
    First point: Data is updated creating the database with 14 entries
        - once the second monday has been reach, remove previous 7 days and update with the next 7 days
    
    Second point: what happens if any day has been updating or shift has been change?
        - then i need to have a checker function: if no shift has been set, remove no shift and add shift,
        - if shift is already present, remove shift start and end time and update new shift start and end time.

    Seems easy enough being typed, need to learn notion api and how to update, remove times.
    also i want to learn about branching from main to learn about about github repository and learning to actually SWE
    big big project, class as started so project will inevitably slow down. But project is to fun to stop now.

"""
