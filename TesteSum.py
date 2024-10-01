# Criar uma lista com os números 5, 10 e 20
numeros = [5, 10, 20]

# Executar a função sum utilizando a lista como argumento
resultado = sum(numeros)

# Verificar se o resultado da soma é 35 (esperado sucesso)
if resultado == 35:
    print("Sucesso: A soma é 35.")
else:
    print("Erro: A soma não é 35.")

# Verificar se o resultado da soma é diferente de 35 (esperado erro)
if resultado != 35:
    print("Erro: A soma é diferente de 35.")
else:
    print("Sucesso: A soma é 35.")