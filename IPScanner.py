import subprocess
import re

first = input("Enter the start of the IP range")
last = input("Enter the end of the IP range")

def get_host(x):
    dot_counter = 0
    pos_counter = 0
    for i in x:
        if i == ".":
            dot_counter = dot_counter + 1
        if dot_counter == 3:
            return (x[0:pos_counter+1])