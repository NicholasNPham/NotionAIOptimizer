# Python AI Schedule Optimizer

## 📌 Goal
This project creates an application that uses AI to optimize my schedule, improving productivity and workflow.

The AI analyzes events, tasks, and priority levels from a Notion database and provides suggestions to improve efficiency.  
Execution phases:  
1. **Manual file run** (current)  
2. **Daemon automation**  
3. **Windows Task Scheduler research**  

The AI will also be capable of reading websites based on given information to plan the next day, which I can then review and adjust.

---

## 1️⃣ PHASE 1:

---

## 📂 Data Sources
- **Primary Source:** Notion database containing:  
  - Events  
  - Tasks  
  - Priority levels  

- **Secondary Source:** Employee portal (web scraping with Selenium).  
  - Selenium securely logs in and collects work schedules.

## ⚙️ Workflow
1. **Scrape Work Schedule**  
   - Automate login with Selenium.  
   - Scrape:  
     - Shift times (e.g., `5:30 AM - 1:30 PM`)  
     - Date (e.g., `8-11`)  
     - Hours worked (e.g., `8 hs`)  

2. **Data Processing**  
   - Configured to match how the code is currently structured.  
   - Convert `hours` strings → floats.  
   - Convert `date` strings → ISO format (`YYYY-MM-DD`).  
   - Split shift string → `start time` and `end time`.  
   - Combine date + time → **time blocks** for Notion.  

3. **Notion Database**  
   - **Always handles removing outdated entries and updating changes smoothly.**  
   - **Status property** planned for a future phase.  
   - Future iterations will include coding shift types:  
     - Working  
     - No scheduled shifts  
     - Day off

---

## 🗓 Key Milestones
- **Aug 13, 2025** → Completed web scraping of employee website. Next step: importing into Notion.  
- **Aug 19, 2025** → Added ISO date conversion. Next: generate start/end datetime objects.  
- **Aug 22, 2025** → Optimized code. `timeBlock` and `scrapeWeek` ready for Notion automation. Lesson: AI guides, but coding done manually for learning and control.  
- **Aug 31, 2025** → Bulk of scraping done. Working on naming shifts correctly for proper Notion import.  
- **Sep 1, 2025** → Phase 1 complete. Phase 2: Manual file run → Daemon → Task Scheduler research.  

---

## 2️⃣ PHASE 2:

---
## ⚙️ Workflow
1. **Desktop Shortcut for Tkinter App**
- Create a shortcut on your desktop that directly runs the Python Tkinter application (`.py` file).
- Steps:
  1. Ensure Python is installed and the `tkinter.py` file runs correctly.
  2. Create a new shortcut on your desktop.
  3. Set the target to: `python "path TBD"`.
  4. assign a custom icon for the shortcut.
- Double-clicking the shortcut launches the Tkinter app without opening the terminal manually.

2. **Tkinter App**
- A simple GUI to manage background processes with a clean, user-friendly interface.
- Features:
  - **Run** and **Kill** buttons to start or stop the selected process.
  - **Dropdown menu** to choose the type of background process (e.g., Daemon).
  - Designed for easy expansion to add more process types in the future.
- Provides a visual way to control automation scripts without using the terminal.

3. **Python Daemon**  

- **Purpose:** Create a background script to run `main.py` automatically during specific system events, such as:  
  - Waking from sleep  
  - Logging on  
  - Unlocking the computer  
  - This will be the **first evolution of automation** beyond manual execution.  

---

## 📚 References
- [PEP 8 Python Style Guide](https://peps.python.org/pep-0008/)  
- [Selenium Tutorial (YouTube)](https://www.youtube.com/watch?v=NB8OceGZGjA)  
- [Notion API Documentation](https://developers.notion.com/docs)  
- [Creating Desktop Apps With Python](https://www.youtube.com/watch?v=PdsoDG0GKdA)  
- [Daemon Processes In Python](https://superfastpython.com/daemon-process-in-python/) 
- [Tkinter](https://docs.python.org/3/library/tkinter.html) 

---

## 📝 Notes
- Currently triggered **manually**, with planned Daemon and Task Scheduler research.  
- Working on datetime values into Notion from `reversed dictSchedule`.  
- **Database rules:**  
  - Always maintain 14 entries.  
  - When second Monday is reached → remove last 7 days, add next 7.  
  - If shift changes:  
    - No shift set → remove placeholder + add new.  
    - Shift already set → update with new start/end.  
- Requires **Notion API** mastery (create, update, delete).  
- Started new branch: **`test-branchV2`** for branching practice.  
- Pace may slow due to classes, but this remains a long-term project that’s *too fun to stop*.  

---

