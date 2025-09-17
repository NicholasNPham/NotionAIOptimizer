from win32com.client import Dispatch

#breaks bad

shell = Dispatch("WScript.Shell")
shortcut = shell.Run("python main.py")
shortcut.Execute()




# Main Function to Run
def createShortcut(path=None, name=None, icon=None, terminal=None):
    pathDirectory = path
    desktopName = name
    iconFile = icon
    terminalBool = terminal
    return pathDirectory, desktopName, iconFile, terminalBool
