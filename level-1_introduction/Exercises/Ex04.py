

# *Atividade 1*

pessoa = {'nome':'Ana Luisa', 'idade':12, 'cidade':'cidade_pessoa'}

# para teste
print(f'{pessoa}')

# *Atividade 2*

pessoa['idade'] = 21
# Para teste 
print(f'{pessoa['idade']}')

pessoa['profissao'] = 'Secretaria'
# para teste
print(f'{pessoa['profissao']}')

del pessoa['cidade']
# para teste 
print(f'{pessoa}')

# *Atividade 3*

numeros_quadrados = {x: x**2 for x in range(1,6)}
print(numeros_quadrados)

#  *Atividade 4*

chaves = {1:'chave1', 2:'chave2', 3:'chave3'}

busca = int(input('Digite o número da chave que você busca (1,2,3): '))

if busca in chaves: 
    print(f'A chave {busca} foi encontrada COM SUCESSO!')
else: 
    print(f'A chave {busca} NÃO foi ancontrada!')  

#  *Atividade 5*  

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."

contagem_palavras = {}
quantidade_palavras = 0

palavras = frase.split()

for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    quantidade_palavras += 1

print(contagem_palavras)
print(f'A quantidade das palavras que aparecem é: {quantidade_palavras}')