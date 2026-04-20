# Atividade 1
print('Listas para coisas!')

numeros = [1,2,3,4,5,6,7,8,9,10]

nomes = ['Ana Luisa', 'Itallo', 'Izadora']

data = [2007, 2026]

print(f'Lista de números: {numeros}')

print(f'Lista de nomes: {nomes}')

print(f'Lista de datas: {data}')

# Atividade 2

lugares_a_visitar = []

cadastrar_lugares = input('Digite lugares que você quer cadastrar: ')
lugares_a_visitar.append(cadastrar_lugares)

print('Lista de Lugares para você vizitar')
for lugares in lugares_a_visitar:
    print(f'{lugares_a_visitar}\n')

# Atividade 3

soma_impares = 0

for i in range(1, 11, 2):
    soma_impares += i

print(soma_impares)

# Atividade 4

for i in range(10, 0, -1):
    print(f'{i}')

# Atividade 5

num = int(input('Digite um número inteiro: '))

for i in range(1, 11):
    tabuada = num * i
    print(f'{num} x {i} = {tabuada}')

# Atividade 6 (possivel melhorar: sistema de adição pelo próprio usuário)

numeros = [1,5,7,8,4,2,3,10]

soma = 0

try:
    for i in numeros:
        soma += i
        

except Exception as e: 
    print(f'Ocorreu um erro no seu programa. Erro: {e}')

print(f'A soma dos números dessa lista é: {soma}')

#Atividade 7

numeros = [10, 15, 14, 7, 80]
soma = 0


try:
    for valor in numeros:
        soma += valor 
    
    media = soma / len(numeros)

    print(f"A média dos valores da lista é: {media}")

except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média")

except Exception as e:
    print(f"Ocorreu um erro: {e}")