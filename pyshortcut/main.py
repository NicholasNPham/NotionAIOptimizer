import win32com.client

# Testing Functionality
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut( r"C:\Users\phamn\OneDrive\Desktop\DAEMON.lnk")
shortcut.TargetPath = r"C:\Users\phamn\AppData\Local\Programs\Python\Launcher\pyw.exe" # Change between py.exe for show and pyw.exe to not show
shortcut.Arguments = r"E:\PycharmProjects\NotionAIOptimizer\DAEMON\interface.py"
shortcut.WorkingDirectory = r"E:\PycharmProjects\NotionAIOptimizer\DAEMON"
shortcut.save()

# Main Function to Run
def createPythonShortcut(path=None, name=None, icon=None, terminal=None):

    shell = win32com.client.Dispatch("WScript.Shell")
    lnkFileLocation = rf"{shell.SpecialFolders("Desktop")}" + rf"\{name}.lnk"

    pathDirectory = path
    desktopName = name
    iconFile = icon
    terminalBool = terminal
    return lnkFileLocation

# Testing Main Function
print(createPythonShortcut(name="test"))
