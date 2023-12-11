from rUSER import*


def menu_user(news):
    while True:
        print('_' * 26)
        print(
            '[1]Buscar\n'
            '[2]Comentar\n'
            '[3]Curtir\n'
            '[4]Listar\n'
            '[5]Logout'
        )
        print('_' * 26)
        choice = input()
        if choice == '1':
            user_search_news(news)

        elif choice == '2':
            user_comment_news(news)

        elif choice == '3':
            user_like_news(news)

        elif choice == '4':
            user_list_news(news)

        elif choice == '5':
            break

        else:
            print('Opção inválida.')
