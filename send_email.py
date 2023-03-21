import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "anorboboyev39@gmail.com"
password = "mdswnwsvvushvgqk"
reciever = "anorboboyev39@gmail.com"

context = ssl.create_default_context()

message = """
Hey!
How are you?
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, reciever, message)