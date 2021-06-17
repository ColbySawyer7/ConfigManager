#INSTALLATION SCRIPT
import subprocess
import sys

assert sys.version_info >= (2,5)

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Update to Python3 (if not)
# Install Netmiko
install('netmiko')
# Install GitPython
install('GitPython')
# Install Other Depen. 
install('argparse')
install('getpass')