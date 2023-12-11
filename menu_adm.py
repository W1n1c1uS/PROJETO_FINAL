from rADM import *


def menu_adm(news, id, usuario):
    while True:
        print('_' * 26)
        print(
            '[1]Inserir\n'
            '[2]Listar\n'
            '[3]Excluir\n'
            '[4]Editar\n'
            '[5]Buscar\n'
            '[6]Salvar\n'
            '[7]Logout'
        )
        print('_' * 26)
        choice = input()
        if choice == '1':
            adm_insert_news(news, id, usuario)

        elif choice == '2':
            adm_list_news(news, usuario)

        elif choice == '3':
            adm_remove_news(news, usuario)

        elif choice == '4':
            adm_edit_news(news, usuario)

        elif choice == '5':
            adm_search_news(news)

        elif choice == '6':
            salvar_arquivo(news, usuario)

        elif choice == '7':
            break

        else:
            print('Opção inválida.')
