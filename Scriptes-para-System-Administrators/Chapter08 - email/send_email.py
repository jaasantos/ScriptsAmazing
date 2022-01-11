'''

import smtplib
from email.mime.text import MIMEText
import getpass

host_name = 'smtp.gmail.com'
port = 465
u_name = 'sangames11@gmail.com/emailid'
password = getpass.getpass()
sender = 'san'
receivers = ['sangames11@gmail.com', 'sangames10@gmail.com']

text = MIMEText('Test mail')
text['Subject'] = 'Test'
text['From'] = sender
text['To'] = ', '.join(receivers)

s_obj = smtplib.SMTP_SSL(host_name, port)
s_obj.login(u_name, password)
s_obj.sendmail(sender, receivers, text.as_string())
s_obj.quit()
print("Mail sent successfully")



'''


import smtplib
import email.message

def enviar_email():
    corpo_email = ('olá, estamos fazendo testes de email automático')
    msg = email.message.Message()
    msg['Subject'] = "TESTE"
    msg['From'] = "sangames11@gmail.com"
    msg['To'] = 'sandro130617@gmail.com'
    password = 'Futebol@13'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()
