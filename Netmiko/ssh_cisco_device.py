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

connect = ConnectHandler(**network_device)

connect.enable()

sh_vlan_brf = "Show vlan brief"

print(connect.send_command(sh_vlan_brf))

interface = input("Enter the interface you want to show (ex: GigabitEthernet 1/0/)")
sh_ip_interface = f"sh ip interface {interface}"

first_port = 10
last_port = 20

for port in range(first_port, last_port+1):
    print(connect.send_command(sh_ip_interface + str(port)))