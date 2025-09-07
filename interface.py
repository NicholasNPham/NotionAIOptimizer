import tkinter as tk
from tkinter import ttk
import time

# Display Settings
root = tk.Tk()
root.title("Background Process")
root.geometry("300x100")
root.configure(background="#222222")

# Show Function to display text
def show():
    if comboBox.get() == "Choose a Process...":
        label.config(text="ERROR: CHOOSE A PROCESS")
    elif comboBox.get() == "DAEMON":
        label.config(text="DAEMON PROCESS RUNNING")
    else:
        label.config(text="ERROR: PROCESS NOT DEVELOPED")

def remove():
    if comboBox.get() == "Choose a Process...":
        label.config(text="ERROR: NOTHING TO TERMINATE")
    elif comboBox.get() == "DAEMON":
        label.config(text="DAEMON PROCESS TERMINATED")
    else:
        label.config(text="ERROR: PROCESS NOT DEVELOPED")

# Dropdown Options
process = ["DAEMON", "option2"]

# Dropdown Menu
comboBox = ttk.Combobox(root, values=process)
comboBox.set("Choose a Process...")
comboBox.pack()

# Button
buttonFrame = tk.Frame(root, bg="#222222")
buttonFrame.pack()

startButton = tk.Button(buttonFrame, text="START", command=show)
startButton.pack(side=tk.LEFT, padx=5, pady=5)

terminateButton = tk.Button(buttonFrame, text="TERMINATE", command=remove)
terminateButton.pack(side=tk.LEFT, padx=5, pady=5)

#Display text after button is pressed
label = tk.Label(root, text=" ", background="#222222", fg="white")
label.pack()

root.mainloop()