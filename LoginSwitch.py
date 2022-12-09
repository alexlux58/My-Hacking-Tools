from netmiko import ConnectHandler

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



connect_to_device = ConnectHandler(**network_device)
connect_to_device.enable()