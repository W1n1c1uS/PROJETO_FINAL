#def usada na def user_search_news
def comment(news, id_for_add_comment):
    comentario = input('Comentário:')
    for x, y in news.items():
        if id_for_add_comment in y:
            news[x][id_for_add_comment][2].append(comentario)
            print('\033[92mComentário adicionado\033[0m')


#essa def serve para o usuário buscar uma noticia
def user_search_news(news):
    for a, b in news.items():
        for c, d in b.items():
            print(f"Autor: {a} \nID: {c} \nTítulo: {d[0]}")
            print('_' * 26)

    while True:
        found = False
        id_to_search = int(input('Informe o ID da notícia para buscá-la:'))
        for x, y in news.items():
            if id_to_search in y:
                print(f'\033[96mAutor: {x}\033[0m')
                print(f'Título: {y[id_to_search][0]}')
                print(f'Artigo: {y[id_to_search][1]}')
                print('_' * 26)
                found = True
                comment_question = input('Deseja fazer um comentário? [sim/nao]')
                if comment_question == 'sim':
                    comment(news, id_to_search)
                    junk = input('Deseja fazer outro comentário? [sim/nao]')
                    if junk == 'sim':
                        comment(news, id_to_search)

        if not found:
            print('\033[91mID inexistente!\033[0m')

        break


#essa def serve para o usuário comentar na notícia
def user_comment_news(news):
    for a, b in news.items():
        for c, d in b.items():
            print(f"Autor: {a} \nID: {c} \nTítulo: {d[0]}")
            print('_' * 26)

    while True:
        found = False
        comment_id = int(input('Informe o ID da notícia para comentar:'))
        comentario = str(input('Comentário:'))
        for x, y in news.items():
            if comment_id in y:
                news[x][comment_id][2].append(comentario)
                print('\033[92mComentário adicionado\033[0m')
                found = True
                junk = input('Deseja fazer outro comentário? [sim/nao]')
                if junk == 'sim':
                    comment(news, comment_id)

        if not found:
            print('\033[91mID inexistente!\033[0m')

        break


#essa def serve para o usuário curtir a notícia
def user_like_news(news):
    for a, b in news.items():
        for c, d in b.items():
            print(f"Autor: {a} \nID: {c} \nTítulo: {d[0]}")
            print('_' * 26)

    while True:
        found = False
        like_id = int(input('Informe o ID da noticia para curti-la:'))
        for x, y in news.items():
            if like_id in y:
                news[x][like_id][3].append('❤️')
                print('\033[92mCurtida adicionada!\033[0m')
                found = True

        if not found:
            print('\033[91mID inexistente!\033[0m')

        break


#essa def serve para o usuário listar as notícias

def ordenar_curtidas(news):
    lista_curtidas = []
    for x, y in news.items():
        pass
        for a, b in y.items():
            #print(a, b)
            curtidas = len(b[3])
            lista_curtidas.append(curtidas)
            n = len(lista_curtidas)
            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    if lista_curtidas[j] < lista_curtidas[j + 1]:
                        lista_curtidas[j], lista_curtidas[j + 1] = lista_curtidas[j + 1], lista_curtidas[j]
    lista_curtidas = list(set(lista_curtidas))
    lista_curtidas = lista_curtidas[::-1]
    return lista_curtidas


def user_list_news(news):
        for x, y in news.items():
            for z in y:
                for i in ordenar_curtidas(news):
                    if len(y[z][3]) == i:
                        print(f'Autor: {x}')
                        print(f'Publicado em {y[z][4]}')
                        print(f'Título: {y[z][0]}')
                        print(f'Artigo: {y[z][1]}')
                        comment = ', '. join(y[z][2])
                        print(f'Comentários: {comment}') if comment else ''
                        print(f'{i}❤️')
                        #print(f'{len(y[3])}❤️')
                        print('_'*26)
        else:
            print('Esse usuário não possui publicações')
'''def user_list_news(news):
    for x, y in news.items():
        print(f'Autor: {x}')
        for z in y:
            print(f'Publicado em {y[z][4]}')
            print(f'Título: {y[z][0]}')
            print(f'Artigo: {y[z][1]}')
            a = ', '.join(y[z][2])
            print(f'Comentários: {a}') if comment else ''
            print(f'{len(y[z][3])}❤️')
            print('_' * 26)'''



