import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def sendkindle():

    def read_creds():
        user = pw = ""
        with open("credentials.txt", "r") as f:
            file = f.readlines()
            user = file[0].strip()
            pw = file[1].strip()
        return user, pw


    def read_receiver():
        receiver = ""
        with open("receiver.txt", "r") as f:
            file = f.readlines()
            receiver = file[0].strip()
        return receiver


    port = 465

    sender, password = read_creds()
    receive = read_receiver()

    message = MIMEMultipart('mixed')
    message['Subject'] = 'MOBI File'
    msg_content = '<h4>Hello,<br> Delivering to you this MOBI File. Happy Reading!</h4>\n'
    body = MIMEText(msg_content, 'html')
    message.attach(body)


    mobi_path = "/Users/jennifersequina/Downloads/mobi_kindle/Loveless_-_Alice_Oseman.mobi"
    mobi = MIMEApplication(open(mobi_path, 'rb').read())
    mobi.add_header('Content-Disposition', 'attachment', filename="Loveless_-_Alice_Oseman.mobi")
    message.attach(mobi)


    context = ssl.create_default_context()

    print("Starting to send")

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receive, message.as_string())

    print("Email sent!")
