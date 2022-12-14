'''
   _____  .__                  .____                                                                
  /  _  \ |  |   ____ ___  ___ |    |    __ _____  ___                                              
 /  /_\  \|  | _/ __ \\  \/  / |    |   |  |  \  \/  /                                              
/    |    \  |_\  ___/ >    <  |    |___|  |  />    <                                               
\____|__  /____/\___  >__/\_ \ |_______ \____//__/\_ \                                              
        \/          \/      \/         \/           \/                                              
_________                                           .___ _________                __                
\_   ___ \  ____   _____   _____ _____    ____    __| _/ \_   ___ \  ____   _____/  |_  ___________ 
/    \  \/ /  _ \ /     \ /     \\__  \  /    \  / __ |  /    \  \/_/ __ \ /    \   __\/ __ \_  __ \
\     \___(  <_> )  Y Y  \  Y Y  \/ __ \|   |  \/ /_/ |  \     \___\  ___/|   |  \  | \  ___/|  | \/
 \______  /\____/|__|_|  /__|_|  (____  /___|  /\____ |   \______  /\___  >___|  /__|  \___  >__|   
        \/             \/      \/     \/     \/      \/          \/     \/     \/          \/     

'''

network_scan_description = '''
nmap -h

Usage: nmap [Scan Type(s)] [Options] {target specification}
TARGET SPECIFICATION:
  Can pass hostnames, IP addresses, networks, etc.
  Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
  -iL <inputfilename>: Input from list of hosts/networks
  -iR <num hosts>: Choose random targets
  --exclude <host1[,host2][,host3],...>: Exclude hosts/networks
  --excludefile <exclude_file>: Exclude list from file
HOST DISCOVERY:
  -sL: List Scan - simply list targets to scan
  -sn: Ping Scan - disable port scan
  -Pn: Treat all hosts as online -- skip host discovery
  -PS/PA/PU/PY[portlist]: TCP SYN/ACK, UDP or SCTP discovery to given ports
  -PE/PP/PM: ICMP echo, timestamp, and netmask request discovery probes
  -PO[protocol list]: IP Protocol Ping
  -n/-R: Never do DNS resolution/Always resolve [default: sometimes]
  --dns-servers <serv1[,serv2],...>: Specify custom DNS servers
  --system-dns: Use OS's DNS resolver
  --traceroute: Trace hop path to each host
SCAN TECHNIQUES:
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags <flags>: Customize TCP scan flags
  -sI <zombie host[:probeport]>: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b <FTP relay host>: FTP bounce scan
PORT SPECIFICATION AND SCAN ORDER:
  -p <port ranges>: Only scan specified ports
    Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
  --exclude-ports <port ranges>: Exclude the specified ports from scanning
  -F: Fast mode - Scan fewer ports than the default scan
  -r: Scan ports consecutively - don't randomize
  --top-ports <number>: Scan <number> most common ports
  --port-ratio <ratio>: Scan ports more common than <ratio>
SERVICE/VERSION DETECTION:
  -sV: Probe open ports to determine service/version info
  --version-intensity <level>: Set from 0 (light) to 9 (try all probes)
  --version-light: Limit to most likely probes (intensity 2)
  --version-all: Try every single probe (intensity 9)
  --version-trace: Show detailed version scan activity (for debugging)
SCRIPT SCAN:
  -sC: equivalent to --script=default
  --script=<Lua scripts>: <Lua scripts> is a comma separated list of
           directories, script-files or script-categories
  --script-args=<n1=v1,[n2=v2,...]>: provide arguments to scripts
  --script-args-file=filename: provide NSE script args in a file
  --script-trace: Show all data sent and received
  --script-updatedb: Update the script database.
  --script-help=<Lua scripts>: Show help about scripts.
           <Lua scripts> is a comma-separated list of script-files or
           script-categories.
OS DETECTION:
  -O: Enable OS detection
  --osscan-limit: Limit OS detection to promising targets
  --osscan-guess: Guess OS more aggressively
TIMING AND PERFORMANCE:
  Options which take <time> are in seconds, or append 'ms' (milliseconds),
  's' (seconds), 'm' (minutes), or 'h' (hours) to the value (e.g. 30m).
  -T<0-5>: Set timing template (higher is faster)
  --min-hostgroup/max-hostgroup <size>: Parallel host scan group sizes
  --min-parallelism/max-parallelism <numprobes>: Probe parallelization
  --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>: Specifies
      probe round trip time.
  --max-retries <tries>: Caps number of port scan probe retransmissions.
  --host-timeout <time>: Give up on target after this long
  --scan-delay/--max-scan-delay <time>: Adjust delay between probes
  --min-rate <number>: Send packets no slower than <number> per second
  --max-rate <number>: Send packets no faster than <number> per second
FIREWALL/IDS EVASION AND SPOOFING:
  -f; --mtu <val>: fragment packets (optionally w/given MTU)
  -D <decoy1,decoy2[,ME],...>: Cloak a scan with decoys
  -S <IP_Address>: Spoof source address
  -e <iface>: Use specified interface
  -g/--source-port <portnum>: Use given port number
  --proxies <url1,[url2],...>: Relay connections through HTTP/SOCKS4 proxies
  --data <hex string>: Append a custom payload to sent packets
  --data-string <string>: Append a custom ASCII string to sent packets
  --data-length <num>: Append random data to sent packets
  --ip-options <options>: Send packets with specified ip options
  --ttl <val>: Set IP time-to-live field
  --spoof-mac <mac address/prefix/vendor name>: Spoof your MAC address
  --badsum: Send packets with a bogus TCP/UDP/SCTP checksum
OUTPUT:
  -oN/-oX/-oS/-oG <file>: Output scan in normal, XML, s|<rIpt kIddi3,
     and Grepable format, respectively, to the given filename.
  -oA <basename>: Output in the three major formats at once
  -v: Increase verbosity level (use -vv or more for greater effect)
  -d: Increase debugging level (use -dd or more for greater effect)
  --reason: Display the reason a port is in a particular state
  --open: Only show open (or possibly open) ports
  --packet-trace: Show all packets sent and received
  --iflist: Print host interfaces and routes (for debugging)
  --append-output: Append to rather than clobber specified output files
  --resume <filename>: Resume an aborted scan
  --stylesheet <path/URL>: XSL stylesheet to transform XML output to HTML
  --webxml: Reference stylesheet from Nmap.Org for more portable XML
  --no-stylesheet: Prevent associating of XSL stylesheet w/XML output
MISC:
  -6: Enable IPv6 scanning
  -A: Enable OS detection, version detection, script scanning, and traceroute
  --datadir <dirname>: Specify custom Nmap data file location
  --send-eth/--send-ip: Send using raw ethernet frames or IP packets
  --privileged: Assume that the user is fully privileged
  --unprivileged: Assume the user lacks raw socket privileges
  -V: Print version number
  -h: Print this help summary page.
EXAMPLES:
  nmap -v -A scanme.nmap.org
  nmap -v -sn 192.168.0.0/16 10.0.0.0/8
  nmap -v -iR 10000 -Pn -p 80
                            '''
                            
essential_commands_text = '''
Basic Nmap Scan (nmap <IP>)
OS Enumeration (nmap <IP> -O)
Scan all TCP ports (nmap <IP> -p-)
Default scripts (nmap <IP> -sC)
All Scans with Verbose explenation (nmap -vv -A <IP>)
'''

from tkinter import *
from tkinter import scrolledtext
import nmap

class Window:
    def __init__(self, title, icon="images/icon.ico", geometry="1100x1100"):
        
        self.tk = Tk()
        self.tk.title(title)
        self.tk.iconbitmap(icon)
        self.tk.geometry(geometry)
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        
        self.module_description_frame = LabelFrame(self.tk, text="Module Description", padx=5, pady=5,font = ("Times New Roman", 16), background = 'white', foreground = "black")
        self.module_description_frame.grid(row=0, column=0, columnspan=2)

        self.decription_text = scrolledtext.ScrolledText(self.module_description_frame, wrap = WORD, width=60, height=50, font = ("Times New Roman", 12))
        self.decription_text.grid(pady=10, padx=10)
        print(network_scan_description)
        self.decription_text.insert(INSERT, network_scan_description)
        self.decription_text.focus()
        
        self.network_scan_button = Button(self.tk, text="Network Scan", padx=50, pady=50, command=self.ScanWindow, fg="black", bg="white")
        self.network_scan_button.grid(row=0, column=3, columnspan=2, padx=50, pady=50)
        
        self.scanner = nmap.PortScanner()
    
    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", self.state)
        return "break"
    
    def ScanWindow(self):
        self.scan_window = Toplevel()
        self.scan_window.geometry("600x600")
        self.IP_entry = Entry(self.scan_window, width=50)
        self.IP_entry.grid(row=0, column=0, columnspan=2, pady=10)
        # self.IP_entry.insert(0, "Target IP: ")
        self.basic_scan_button = Button(self.scan_window, text="Basic Scan", pady=10, command=self.basic_scan, fg="black", bg="blue")
        self.basic_scan_button.grid(row=1, column=0, columnspan=1)
        self.essential_commands_frame = LabelFrame(self.scan_window, text="Essential Commands", padx=5, pady=5,font = ("Times New Roman", 16), background = 'white', foreground = "black")
        self.essential_commands_frame.grid(row=2, column=0, columnspan=2)
        self.decription_text = Text(self.essential_commands_frame, wrap = WORD, width=60, height=50, font = ("Times New Roman", 12))
        self.decription_text.grid(row=3, column=0, columnspan=2, pady=10)
        self.decription_text.insert(INSERT, essential_commands_text)
        self.decription_text.focus()
        
    def basic_scan(self):
        print(type(self.IP_entry.get()))
        print("Nmap Version: ", self.scanner.nmap_version())
        self.scanner.scan(self.IP_entry.get(), "1-1024", "-v")
        print(self.scanner.scaninfo())
        print("IP Status: ", self.scanner[self.IP_entry.get()].state())
        print(self.scanner[self.IP_entry.get()].all_protocols())
        print("Open Ports: ", self.scanner[self.IP_entry.get()]["tcp"].keys())
        
        
    def OS_enumeration(self):
        pass
        

if __name__ == "__main__":
    root = Window(title="Command Center")
    root.tk.mainloop()


