import os
import time

# App para Linux

restaurantes = [{"nome":"Praça", "categoria":"Japonesa", "ativo":False},
                {"nome":"Pizza Suprema", "categoria":"Pizza", "ativo":True},
                {"nome":"Cantina", "categoria":"Italiana", "ativo":False}]

def exibir_nome_do_programa():
      print('''    
       
░█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ░█▀▀▀ █─█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
─▀▀▀▄▄ █▄▄█ █▀▀▄ █──█ █▄▄▀ 　 ░█▀▀▀ ▄▀▄ █──█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
░█▄▄▄█ ▀──▀ ▀▀▀─ ▀▀▀▀ ▀─▀▀ 　 ░█▄▄▄ ▀─▀ █▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀ ▀▀▀
      
      ''') # sempre que quiser também pular uma linha ou formatação para o print pode se usar a aspas triplas ''' ''' (vou colocar um exemplo de formatação nbo final nas anotações)

def exibir_opcoes():
      #i \n pula uma linha no terminal
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. ativar restaurante')
      print('4. sair') 
      print('5. Reiniciar \n')

def finalizar_app():
    print('Encerrando o App...')
    time.sleep(3)
    exibir_subtitulo('App Finalizado com sucesso!')
    time.sleep(2)
    os.system('clear')
    #aqui estou DEFININDO uma FUNÇÃO para o item 4

def reiniciar_app():
   print('Reiniciando o App...')
   time.sleep(3)
   os.system('clear')
   os.system('python3 app.py')
   # Para o app de windows modificar para ('python app.py')

def opcao_invalida():
   print('Essa opção que você digitou é invalida...\n')
   voltar_ao_menu()
  
def voltar_ao_menu():
   input('\nDigite uma tecla qualquer para retornar ao menu principal!')
   print('Carregando...')
   time.sleep(3)
   main()

def exibir_subtitulo(texto):
   os.system('clear')
   print(texto)  
   print() 

def cadastrar_novo_restaurante():
   exibir_subtitulo('Cadastro de novos restaurantes')
   nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
   restaurantes.append(nome_do_restaurante)
   print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
   voltar_ao_menu()

def listar_restaurantes():
   exibir_subtitulo('Listagem de Restaurantes')
   for restaurante in restaurantes:
      # criando as categorias para listagem no app usando a propria lista
      nome_restaurante = restaurante ['nome']
      categoria_restaurantes = restaurante ['categoria']
      ativo_restaurantes = restaurante ['ativo']
      # Print para a visualização da lista
      print(f'- {nome_restaurante} | {categoria_restaurantes} | {ativo_restaurantes}')
   voltar_ao_menu()


def escolher_opcao():
    try:
      opcao_escolha = int(input('Escolha uma opção: '))

      if opcao_escolha == 1:
        print('Cadastrar restaurante')
        cadastrar_novo_restaurante()

      elif opcao_escolha == 2:
        listar_restaurantes()

      elif opcao_escolha == 3:
        print('Ativar restaurantes')

      elif opcao_escolha == 4:
        finalizar_app()

      elif opcao_escolha == 5:
        reiniciar_app()

      else:
        opcao_invalida()

    except ValueError:  # coloquei o ValueError para ser expecifico mas o código funciona sem o ValueError
      opcao_invalida() 

def main():
    os.system('clear')
    # para o app no windows modificar para ('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()