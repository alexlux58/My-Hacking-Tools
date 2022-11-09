import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Initialize SMTP 
# server = smtplib.SMTP("smtp.office365.com", 587)
server = smtplib.SMTP("smtp.gmail.com", 587)

# Start SMTP 
server.ehlo()
server.starttls()

# Get APP Password from Mail provider
with open("password.txt", "r") as f:
	password = f.read()
	
server.login("alexlux58@gmail.com", password)

msg = MIMEMultipart()
msg["From"] = "alexlux58@gmail.com"
msg["To"] = "alexlux@live.com"
msg["Subject"] = "Just a test"

with open("message.txt", "r") as f:
	message = f.read()
	
msg.attach(MIMEText(message, "plain"))

filename = "coding.jpg"
attachment = open(filename, "rb")

p = MIMEBase("application", "octet-stream")
p.set_payload((attachment).read())

encoders.encode_base64(p)
p.add_header("Content-Disposition", f"attachment; filename={filename}")
msg.attach(p)

text = msg.as_string()
server.sendmail("alexlux58@gmail.com", "alexlux@live.com", text)