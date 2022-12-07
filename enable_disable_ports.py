from netmiko import ConnectHandler
import subprocess

ip_addr = input("Enter your devices IP address (ex: 192.168.1.1)")
username = input("Enter your username (ex: ajax66!)")
password = input("Enter your password (ex: Password123!)")
device_type = input("Enter the device type (ex: cisco_ios)")
secret = input("Enter secret (ex: Educate45!)")

network_device = {
    "host": f"{ip_addr}",
    "username": f"{username}",
    "password": f"{password}",
    "device_type": f"{device_type}",
    "secret": f"{secret}",
}

first_port = 1
last_port = 5

connect_to_device = ConnectHandler(**network_device)
connect_to_device.enable()
list_of_commands = ["interface gi 1/0/1", "shut", "end"]
to_execute = connect_to_device.send_command("sh interface gi 1/0/1 status")
print(to_execute)
to_execute = connect_to_device.send_config_set(list_of_commands)
print(to_execute)
to_execute = connect_to_device.send_command("sh interface gi 1/0/1 status")
print(to_execute)

for port in range(first_port, last_port+1):
    list_of_commands = ["interface gi 1/0/" + str(port), "shut"]
    to_execute = connect_to_device.send_config_set(list_of_commands)
    
to_execute = connect_to_device.send_command("sh ip interface brief")
print(to_execute)