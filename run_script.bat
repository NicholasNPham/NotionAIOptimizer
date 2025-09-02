@echo off
REM Go to project folder
cd /d "E:\PycharmProjects\NotionAIOptimizer"

REM Activate venv
call ".venv\Scripts\activate.bat"

REM Run script and log output
python main.py > task_log.txt 2>&1