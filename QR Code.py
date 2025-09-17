import pyqrcode
import png
from qrcode import QRCode

# String com a URL ou texto que você quer transformar em QR Code
qr_string = "https://www.exemplo.com" # Substitua pela sua URL

# Criar objeto QRCode
qr = qrcode.QRCode(filetype=qr_string)

#Gerar e salvar como PNG
qr.png('qrcode_gerado.png' , scale=8
