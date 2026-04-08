import os
import time

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
      print('5 Reiniciar \n')

def finalizar_app():
    print('Encerrando o App...')
    time.sleep(3)
    os.system('cls')
    print('App Finalizado com sucesso!')
    time.sleep(2)
    os.system('cls')
    #os.system('python app.py') REINICIAR
    #aqui estou DEFININDO uma FUNÇÃO para o item 4

def reiniciar_app():
   print('Reiniciando o App...')
   time.sleep(3)
   os.system('cls')
   os.system('python app.py')

def escolher_opcao():
    opcao_escolha = int(input('Escolha uma opção: '))

    if opcao_escolha == 1:
      print('Cadastrar restaurante')
    elif opcao_escolha == 2:
      print('Listar restaurantes')
    elif opcao_escolha == 3:
      print('Ativar restaurantes')
    elif opcao_escolha == 4:
      finalizar_app()
    else:
      reiniciar_app()  

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()