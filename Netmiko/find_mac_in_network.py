from netmiko import ConnectionHandler
import re

mac = input("Enter the Mac address you are looking for")
mac = mac.replace("-", "")