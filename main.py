# =================================
# Configuration Manager
# =================================
# =================================
#Author: 
#   Colby Sawyer
#   Last Updated: 6/17/2021
# =================================
import git, sys, argparse, netmiko, getpass

assert sys.version_info >= (2,5)
# =================================
# =================================
# =================================


# =================================
# =================================
# =================================
def update():
    print("Updating ConfigManager .......")
    git_dir = "https://github.com/ColbySawyer7/ConfigManager.git"
    git.cmd.Git(git_dir).pull()

# =================================
# =================================
# =================================
from netmiko import ConnectHandler
from getpass import getpass

def connect(device):
    print("Connecting to " + device)
    from devices import device
    # Will automatically 'disconnect()'
    with ConnectHandler(**device) as net_connect:
        print(net_connect.find_prompt())
# =================================
# =================================
# =================================
parser = argparse.ArgumentParser(description="Welcome to the Configuration Manager Help")
subparsers = parser.add_subparsers()
parser_update = subparsers.add_parser('update', help='update ConfigManager')
parser_update.set_defaults(func=update)
parser_connect = subparsers.add_parser('connect', help='connect to a device')
parser_connect.set_defaults(func=connect)
args = parser.parse_args()
