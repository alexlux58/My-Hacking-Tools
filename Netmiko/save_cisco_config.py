from netmiko import ConnectHandler
import subprocess

def user_name():
    position_counter = 0
    # result = desktop-hf0tdfv\alex lux
    result = subprocess.getoutput("whoami") 
    for words in result:
        if words == "\\":
            position = position_counter
            break
        position_counter += 1
    return result[position+1:]

local_computer_username = user_name()
print(local_computer_username)


# Create connection to switch/router/firewall/cisco/junyper/hp
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
# Call 'enable()' method to elevate privileges
connect.enable()

sh_env_all = "sh env all"
output = connect.send_command(sh_env_all)

with open("Config.txt", "w") as f:
    f.write("SW1#" + sh_env_all + "\n")
    f.write(output + "\n")