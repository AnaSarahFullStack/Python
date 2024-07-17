#Import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#Criação de um objeto de mensagem
msg= MIMEMultipart()
texto= "Estou enviando um e-mail m Python"

#Parâmetros
senha= "SUA SENHA"
msg['From']= "SEU E-MAIL"
msg['TO']= "E-MAIL DESTINO"
msg['Subject']= "ASSUNTO"

#Criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

#Criação do servidor
server= smtplib.SMTP('smtp.gmail.com:587')
server.starttls()

#Login na conta para envio
server.login(msg['From'],senha)

#Envio da mensagem
server.sendmail(msg['From'],msg['TO'],msg.as_string())

#Encerramento do servidor
server.quit()

print("Mensagem enviada com sucesso")