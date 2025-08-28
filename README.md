# Python AI Schedule Optimizer

## Goal

This project creates an application that uses AI to optimize my schedule, improving productivity and workflow.

The AI will analyze events, tasks, and priority levels from a Notion database (or a local SQL database) and provide suggestions to improve efficiency. Initially, the program will run via manual trigger once per day, with plans to eventually provide **real-time updates**. The AI will also be capable of reading websites based on given information to plan the next day, which I can then review and adjust.

---

## Data Source

* **Primary Source:** Notion database containing:

  * Events
  * Tasks
  * Priority levels
* **Secondary Source:** Employee portal via web scraping with Selenium.
* Selenium will securely log in and collect work schedules.

---

## Project Workflow

1. **Scrape Work Schedule**

   * Selenium automates login to the employee portal.
   * Login credentials are stored securely.
   * Data scraped includes:

     * Shift times (e.g., `5:30 AM - 1:30 PM`)
     * Date (e.g., `8-11`)
     * Hours worked (e.g., `8 hs`)

2. **Data Processing**

   * Convert `hours` strings to floats (removing “hs”).
   * Convert `date` strings to ISO format (`YYYY-MM-DD`) for Notion compatibility.
   * Split shift strings into `start time` and `end time`.
   * Combine date and time to create **time blocks** for the Notion calendar database.

3. **Notion Database**

   * Status property with three states:

     * **Completed/Past:** Shifts that have already occurred
     * **Today:** Current shift
     * **Upcoming/Future:** Future shifts
   * Three types of scheduled shifts:

     * Working
     * No scheduled shifts
     * Day off

---

## Key Milestones

* **August 13, 2025:** Completed web scraping of employee website. Next step is importing the data into Notion.
* **August 19, 2025:** Added function to convert dates to ISO format. Planning to generate start and end datetime objects for time blocks.
* **August 22, 2025:** Optimized code extensively. Most obsolete functions removed. `timeBlock` and `scrapeWeek` are now fully functional and ready for automation in Notion. Key lesson: AI improves productivity and provides guidance, but coding is done manually for learning and control.

---

## References

* [PEP 8 Python Style Guide](https://peps.python.org/pep-0008/)
* [Selenium Tutorial (YouTube)](https://www.youtube.com/watch?v=NB8OceGZGjA)

---

## Notes

## Notes
- Project is triggered **manually once per day** (future: automated at PC startup via Windows Task Scheduler).  
- Currently working on getting datetime values into the database from `reversed dictSchedule` (must be formatted correctly).  
- **Research:**  
  - Database should always hold 14 entries.  
  - When the **second Monday** is reached → remove the previous 7 days and add the next 7 days.  
  - If a shift changes:  
    - If no shift was set → remove “no shift” and add the new shift.  
    - If a shift was already present → remove old start/end times and update with the new ones.  
- Will require learning **Notion API** operations: create, update, and delete entries.  
- Started a new test branch: **`test-branchV2`** to practice Git branching and improve SWE workflow.  
- Project pace may slow due to class schedule, but this remains a long-term project that’s *too fun to stop*.  