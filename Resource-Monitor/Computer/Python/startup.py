import subprocess, psutil

#config variables - these change what the program does
runOHW = False
doUnitTest = True

#OHW_Path should be changed to the path of OpenHardwareMonitor.exe on the system
#It may be different on different computers
#The string should have an r flag to disregard any escape sequences
OHW_Path = r"E:\OpenHWMonitor\OpenHardwareMonitor\OpenHardwareMonitor.exe"

def start():
    """starts the project in accordance with config variables"""
    if runOHW:
        startOHW()

    if doUnitTest:
        unitTest()
    


def isOHWRunning():
    """returns True if OHW is running, otherwise returns False"""
    for proc in psutil.process_iter():
        if proc.name() == "OpenHardwareMonitor.exe":
            return True
    return False

def startOHW():
    """starts Open Hardware Monitor"""
    subprocess.call(["powershell.exe", "Start-Process " + OHW_Path + " -Verb runAs"])

def printProcesses():
    """prints processes currently running"""
    for proc in psutil.process_iter():
        print(proc)


def unitTest():
    """method for testing new methods"""

    startOHW()

    if isOHWRunning():
        print("OHW is running")
    else:
        print("OHW is NOT running")
    #printProcesses()

#run start program
start()

