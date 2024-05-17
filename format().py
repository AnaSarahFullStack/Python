hora=60
minutos=120
segundos=90

print(str(hora)+':'+str(minutos)+':'+str(segundos))

print('{}:{}:{}'.format(hora,minutos,segundos))

#Fomatar saída intuitiva cm printf
print(f'{hora}:{minutos}:{segundos}')

#Especificar largura
print('{:4},{:5}'.format(50,80))

#Valor de ponto flutuante . Determina quantidade de espaços e quantos serão utilizados 
print('{:10.8}'.format(50/20)) 