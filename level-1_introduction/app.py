import os
import time

# App para Linux

restaurantes = [{"nome":"Praça", "categoria":"Japonesa", "ativo":False},
                {"nome":"Pizza Suprema", "categoria":"Pizza", "ativo":True},
                {"nome":"Cantina", "categoria":"Italiana", "ativo":False}]

def exibir_nome_do_programa():
      ''' Essa função é chamada todas as vezes que o menu é chamado, ela é o título do app '''
      print('''    
       
░█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ░█▀▀▀ █─█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
─▀▀▀▄▄ █▄▄█ █▀▀▄ █──█ █▄▄▀ 　 ░█▀▀▀ ▄▀▄ █──█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
░█▄▄▄█ ▀──▀ ▀▀▀─ ▀▀▀▀ ▀─▀▀ 　 ░█▄▄▄ ▀─▀ █▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀ ▀▀▀
      
      ''') # sempre que quiser também pular uma linha ou formatação para o print pode se usar a aspas triplas ''' ''' (vou colocar um exemplo de formatação nbo final nas anotações)

def exibir_opcoes():
      ''' Essa função é para exibir as opções de escolha do usuário '''
      #i \n pula uma linha no terminal
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Alternar estado do restaurante')
      print('4. Sair') 
      print('5. Reiniciar \n')

def finalizar_app():
    ''' Essa função serve para a finalização do código, ou do app no caso. Ele termina o nosso código '''
    print('Encerrando o App...')
    time.sleep(2)
    exibir_subtitulo('App Finalizado com sucesso!')
    time.sleep(2)
    os.system('clear')
    #aqui estou DEFININDO uma FUNÇÃO para o item 4

def reiniciar_app():
   ''' Essa função é para reiniciar o app, caso queria reiniciar tem essa escolha e função '''
   print('Reiniciando o App...')
   time.sleep(2)
   os.system('clear')
   os.system('python3 app.py')
   # Para o app de windows modificar para ('python app.py')

def opcao_invalida():
   ''' Essa função é para quando tiver alguma opação invalida tanto quando colocar nas opções de inicio quanto nas outras abas do app '''
   print('Essa opção que você digitou é invalida...\n')
   voltar_ao_menu()
  
def voltar_ao_menu():
   ''' Essa função serve para voltar ao menu, quando terminar de cadastrar por exemplo o restaurante essa função deve ser chamada para que a pessoa retorne ao inicio '''
   input('\nDigite uma tecla qualquer para retornar ao menu principal!')
   print('Carregando...')
   time.sleep(2)
   main()

def exibir_subtitulo(texto):
   ''' Essa função serve para Exibir o subtitulo, geralmente chamada em toda aba assim que é chamada a escolha das opções '''
   linha = '*' * (len(texto))
   os.system('clear')
   print(linha)
   print(texto) 
   print(linha)
   print() 

def cadastrar_novo_restaurante():
   ''' Essa função é a de cadastros de restaurante, geralmente é chamada quando escolhida nas opções iniciais e ela faz o cadastro de um novo restaurante na lista, com todos os seus atributos do dicionario  '''
   exibir_subtitulo('Cadastro de novos restaurantes')
   nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
   categoria = input(f'Digite a categoria do seu restaurante {nome_do_restaurante}: ')
   dados_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
   restaurantes.append(dados_restaurante)
   print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
   voltar_ao_menu()

def listar_restaurantes(): 
   ''' Essa funçã serve para listar todos os restaurante cadastrados na lista de dicionarios, e aparece também seus atributos  '''
   exibir_subtitulo('Listagem de Restaurantes')

   print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria do restaurante'.ljust(22)} | {'Status'}')
   for restaurante in restaurantes:
      # criando as categorias para listagem no app usando a propria lista
      nome_restaurante = restaurante ['nome']
      categoria_restaurantes = restaurante ['categoria']
      ativo_restaurantes = 'Ativo' if restaurante ['ativo'] else 'Inativo'
      # Print para a visualização da lista
      print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurantes.ljust(20)} | {ativo_restaurantes}')
      # O ljust serve para ajustar as linhas, nesse caso fizemos como se fosse colunas para separação de colunas.
   voltar_ao_menu()

def alternar_estado_restaurante():
   ''' Essa função serve para alterar o estado do restaurante se ele estiver ativo então quando escolhido ele desativa, se desativado quando escolhido ele ativa  '''
   exibir_subtitulo('Alternando o estado do restaurante')
   
   nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
   restaurante_encontrado = False

   for restaurante in restaurantes:
      if nome_restaurante == restaurante ['nome']:
         restaurante_encontrado = True
         restaurante ['ativo'] = not restaurante ['ativo']
         mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
         print(mensagem)
         # Esse termo a cima se chama ternario passamos um if dentro da mensagem, como essa mensagem é para um valor boolean, então podemos fazer duas respostas diferentes 
   if not restaurante_encontrado:
      print('O restaurante não foi encontrado :(')

   voltar_ao_menu()


def escolher_opcao():
    ''' Essa função serve para escolher uma das opções, quando esclhido a opção o programa puxa uma das outras funções ou "Abas" para funcionar o app '''
    try:
      opcao_escolha = int(input('Escolha uma opção: '))

      if opcao_escolha == 1:
        print('Cadastrar restaurante')
        cadastrar_novo_restaurante()

      elif opcao_escolha == 2:
        listar_restaurantes()

      elif opcao_escolha == 3:
        alternar_estado_restaurante()

      elif opcao_escolha == 4:
        finalizar_app()

      elif opcao_escolha == 5:
        reiniciar_app()

      else:
        opcao_invalida()

    except ValueError:  # coloquei o ValueError para ser expecifico mas o código funciona sem o ValueError
      opcao_invalida() 

def main():
    ''' Essa função serve para iniciar ou sempre que o menu é chamado, em alguns caso pode ser chamado no meio do programa em outros pode ser chamado sempre altomaticamente no inicio do programa, ele sempre irá chamar funções principais, como o titúlo, exibir as opções e escolher a opção. '''
    os.system('clear')
    # para o app no windows modificar para ('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()