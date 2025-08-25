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
