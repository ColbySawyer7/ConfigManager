#INSTALLATION SCRIPT
import subprocess
import sys
import git 

assert sys.version_info >= (2,5)

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def updatePy():
    print("Updating ConfigManager .......")

# Update to Python3 (if not)
# Install Netmiko
# Install GitPython
# Install Other Depen. 
