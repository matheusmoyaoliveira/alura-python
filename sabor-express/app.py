import os

restaurantes = []

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

def opçao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def escolher_opçao():
    try:
        opçao_escolhida = int(input('Escolha uma opção: '))
        # opçao_escolhida = int(opçao_escolhida)
            
        if opçao_escolhida == 1:
            print('Cadastrar restaurante')
        elif opçao_escolhida == 2:
            print('Listar restaurantes')
        elif opçao_escolhida == 3:
            print('Ativar restaurante')
        elif opçao_escolhida == 4:
            finalizar_app()
        else:
            opçao_invalida()
    except:
        opçao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opçoes()
    escolher_opçao()

if __name__ == '__main__':
    main()
