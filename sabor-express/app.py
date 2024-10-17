import os

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opçoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    # os.system('clear') no mac
    print('Finalizando o app\n')

def escolher_opçao():
    opçao_escolhida = int(input('Escolha uma opção: '))
    # opçao_escolhida = int(opçao_escolhida)
        
    if opçao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opçao_escolhida == 2:
        print('Listar restaurantes')
    elif opçao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opçoes()
    escolher_opçao()

if __name__ == '__main__':
    main()