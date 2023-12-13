import os
from pathlib import Path
from string import Template
from email.mime.multipart import MIMEmultipart
from email.mime.text import MIMEText
import smtplib

from dotenv import load_dotenv #type: ignore

load_dotenv()

# Caminho do arquivo

CAMINHO_ARQUIVO = pathlib.Path(__file__).parent / 'msg.html'

#dados do remetente
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

#Configurações smtp
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

#Mensagem de texto
with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute('Lucas')

# transformando o email em MIMEmultipart
mime_multipart = MIMEmultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do email.'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_usernamem, smtp_password)
    server.send_message(mime_multipart)
    print('Email enviado com sucesso.')


