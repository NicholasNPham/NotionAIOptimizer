# Python AI Schedule Optimizer

## 📌 Goal
This project creates an application that uses AI to optimize my schedule, improving productivity and workflow.

The AI analyzes events, tasks, and priority levels from a Notion database (or a local SQL database) and provides suggestions to improve efficiency.  
Execution phases:  
1. **Manual file run** (current)  
2. **Daemon automation**  
3. **Windows Task Scheduler research**  

The AI will also be capable of reading websites based on given information to plan the next day, which I can then review and adjust.

---

## 📂 Data Sources
- **Primary Source:** Notion database containing:  
  - Events  
  - Tasks  
  - Priority levels  

- **Secondary Source:** Employee portal (web scraping with Selenium).  
  - Selenium securely logs in and collects work schedules.  

---

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
   - Current focus: **automation** and correct import of shifts.  

---

## 🗓 Key Milestones
- **Aug 13, 2025** → Completed web scraping of employee website. Next step: importing into Notion.  
- **Aug 19, 2025** → Added ISO date conversion. Next: generate start/end datetime objects.  
- **Aug 22, 2025** → Optimized code. `timeBlock` and `scrapeWeek` ready for Notion automation. Lesson: AI guides, but coding done manually for learning and control.  
- **Aug 31, 2025** → Bulk of scraping done. Working on naming shifts correctly for proper Notion import.  
- **Sep 1, 2025** → Phase 1 complete. Phase 2: Manual file run → Daemon → Task Scheduler research.  

---

## 📚 References
- [PEP 8 Python Style Guide](https://peps.python.org/pep-0008/)  
- [Selenium Tutorial (YouTube)](https://www.youtube.com/watch?v=NB8OceGZGjA)  
- [Notion API Documentation](https://developers.notion.com/docs)  

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

