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
parser = argparse.ArgumentParser(description="Welcome to the Configuration Manager")
parser_update = parser.add_argument( '-u', '--update', action='store_true', help='Update ConfigManager')
connection_group = parser.add_mutually_exclusive_group()
parser_connect = connection_group.add_argument('-c','--connect',metavar='', type=str, help='Connect to a device')
parser_connect = connection_group.add_argument('-d','--disconnect',metavar='', type=str, help='Disconnect from a device')
args = parser.parse_args()
#print(args)


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

def connect(device):
    print(" // Connecting to " + device + ".......")
    
    # Will automatically 'disconnect()'
    with ConnectHandler(**device) as net_connect:
        print(net_connect.find_prompt())

# =================================
# =================================
# =================================
def disconnect(device):
    print(" // Disconnecting from " + device + "......")
    


# =================================
# =================================
# =================================
if args.update:
    update()
if args.connect is not None:
    device = args.connect
    connect(device)
if args.disconnect is not None:
    device = args.disconnect
    disconnect(device)