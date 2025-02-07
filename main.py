import random

# Definindo comprimento e as opções que a senha pode ter 
comprimento_senha = 12
opcoes = {
    'incluir_maiusculas': True,
    'incluir_minusculas': True,
    'incluir_numeros': True,
    'incluir_simbolos': True,
}

# Definindo os caracteres que podem ser utilizados
caracteres = ''
if opcoes['incluir_maiusculas']:
    caracteres += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if opcoes['incluir_minusculas']:
    caracteres += 'abcdefghijklmnopqrstuvwxyz'
if opcoes['incluir_numeros']:
    caracteres += '0123456789'
if opcoes['incluir_simbolos']:
    caracteres += '!@#$%^&*()'

# Gerando a senha
senha = ''.join(random.choice(caracteres) for _ in range(comprimento_senha))
print(senha)
