import subprocess

# computer_list = []

print("This script will shut down multiple computers on a domain.")
file_name = input("Enter the name of the text file you want to read the computer IP/Names from.")

with open(file_name, 'r') as f:
    computer_list = f.read().splitlines()
    print("LIST READ: ", computer_list)
    for computer in computer_list: 
        print(subprocess.getoutput("shutdown -m \\\\" + computer + " -f -s -t 0"))