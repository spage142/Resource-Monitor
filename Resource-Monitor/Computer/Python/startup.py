import subprocess, psutil

#config variables - these change what the program does
runOHW = False
doUnitTest = True

def start():
    """starts the project in accordance with config variables"""
    if runOHW:
        startOHW()
    elif doUnitTest:
        unitTest()
    


def isOHWRunning():
    """returns True if OHW is running, otherwise returns False"""
    for proc in psutil.process_iter():
        if proc.name() == "OpenHardwareMonitor.exe":
            return True
    return False

def startOHW():
    """starts Open Hardware Monitor"""
    path = r"D:\Open Hardware Monitor\OpenHardwareMonitor\OpenHardwareMonitor.exe"
    subprocess.call([path])

def printProcesses():
    """prints processes currently running"""
    for proc in psutil.process_iter():
        print(proc)


def unitTest():
    """method for testing new methods"""
    if isOHWRunning():
        print("OHW is running")
    else:
        print("OHW is NOT running")
    #printProcesses()

#run start program
start()

