import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opçoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')
    # os.system('clear') no mac
    

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opçao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_ao_menu_principal()

def escolher_opçao():
    try:
        opçao_escolhida = int(input('Escolha uma opção: '))
        # opçao_escolhida = int(opçao_escolhida)
            
        if opçao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opçao_escolhida == 2:
            listar_restaurantes()
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
