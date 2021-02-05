import smtplib

server = smtplib.SMTP("mail.gmail.com", 587)

server.ehlo()
server.starttls()
server.ehlo()

server.login("theognis1002@gmail.com", "mypass!")

server.sendmail(
    "theognis1002@gmail.com", ["joe123@yahoo.com", "john@gmail.com"], "Email content"
)
