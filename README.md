Title: Python AI Schedule Optimizer

Goal: This project will create an app that will use AI to optimize my schedule created first hand and increase productivity and work flow. 

1. The data supplied from Notion is:
   2. Events, Tasks, and Priority Levels.
2. I will either create my own database or use a pre-existing database based on the Notion API or use SQl (Subject to Change).
3. I want this program to run first off of manual trigger once a day, then eventually
   4. Provide real time updates.
   5. AI will read websites based on given information and plan next day for me to evaluate and continue along.

Notes: 
1. To start this project I need to start off with a "work schedule" notion database
   2. This will be done with Selenium to control the browser and securely login into my employee portal.
   3. Login info will be kept securely and either methods will control website access for me.
   4. This is going to be updated automatically on pc start up with Windows Task Scheduler

Selenium:
Link for Educational Purposes: https://www.youtube.com/watch?v=NB8OceGZGjA

August 13, 2025:
Web scraping my employee website has been done, I now need to move data from the website to Notion Database.

Example:

Shift: 5:30 AM - 1:30 PM - cmp-schedule-item__schedule-content__hours-range
Date: 8-11 - cmp-schedule-item__schedule-date
Hours: 8 - total-hours
Status: Completed 

The Status property will have 3 statuses:
   completed; past,
   today; today shift,
   upcoming; future date based on today's date, import time

Three Type of scheduled shifts:
   working,
   no scheduled shifts,
   Day off.

Notes for Notion Database:
1. The "Hour" string will have to turn into a integer removing "hs" keeping the decimal point
2. The "date" string will have to be converted to a iso format YYYY-MM-DD to allow database read
3. the "shift" string will be split into two strings, example:
   4. '5:30 AM - 2:00 PM'
   5. '5:30 AM' , '2:00 PM'
   6. date + start time, date + end time

After this this will allow me to input data to notion database and create time blocks automatically.

August 19th, 2025:
Added function to turn date into ISO date and it worked well, need to figure out how to create two different time dates that creates start time and end time to create time blocks on notion calendar database.
also going to optimize code to use less lines getting really long. might focus on how code should look like.

Pep 8 formatting for Python Code: https://peps.python.org/pep-0008/