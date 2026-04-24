import time
import os

# Atividade 1 

num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é impar!')

# Atividade 2

nome = input('Digite seu nome: ').upper()

idade = int(input('Digite a sua idade: '))

if idade >= 0 and idade <= 12:
    print(f'{nome} você é uma criança é a sua idade é de {idade} anos')
elif idade >= 13 and idade <= 18:
    print(f'{nome} você é um adolecente e tem {idade} anos')
else:
    print(f'{nome} você já é um adulto e tem {idade} anos')

# Atividade 3

#Banco de dados
id1_nome1 = 'ITALLO'
id1_senha1 = '1234'

nome = input('Digite o seu nome para a verificação: ').upper().strip()
senha = input('Digite sua senha para a verificação: ')

def incorreto():
     time.sleep(3)
     os.system('cls')
     print('Tente novamente colocando o nome e a senha corretamente!')
     print('Reiniciando sistema...')
     time.sleep(3)
     os.system('cls')
     os.system('python Ex02.py')

def correto():
    print('verificando...')
    time.sleep(3)
    os.system('cls')
    print('Suas credenciais estão corretas. Seu acesso foi liberado!')
    time.sleep(3)
    os.system('cls')
    print('''
    ██████████████████████▀██████████████████████████████████████████████████████████████████████
    █▄─▄▄─█▄─▄▄▀█─▄▄─█─▄▄▄▄█▄─▄▄▀██▀▄─██▄─▀█▀─▄██▀▄─████─▄▄▄▄█▄─▄▄─█─▄▄▄─█▄─▄▄▀█▄─▄▄─█─▄─▄─█─▄▄─█
    ██─▄▄▄██─▄─▄█─██─█─██▄─██─▄─▄██─▀─███─█▄█─███─▀─████▄▄▄▄─██─▄█▀█─███▀██─▄─▄██─▄█▀███─███─██─█
    ▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▀''')

if nome == id1_nome1: 
        print('Seu nome está correto!')
        
else:
      print('Sua credencial nome esta incorreta!')
      

if senha == id1_senha1: 
        print('Sua senha está correta!')
        correto()
else:
      print('Sua credencial senha está incorreta!')
      incorreto()


# Atividade 4

x = float(input('Digite o valor de x: '))
y = float(input('Digite o valor de y: '))

if x > 0 and y > 0:
     print(f'Primeiro Quadrante: X: {x} e Y: {y} ')
elif x < 0 and y > 0:
     print(f'Segundo Quadrante: X: {x} e Y: {y} ')
elif  x < 0 and y < 0:
     print(f'Terceiro Quadrante: X: {x} e Y: {y}')
elif x > 0 and y < 0:
     print(f'Quarto Quadrante: X: {x} e Y: {y}')
else:
     print(f'As cordenadas passadas de X: {x} e Y: {y} está no eixo de origem')