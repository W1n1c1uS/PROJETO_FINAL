from register_adm import register_adm
from register_user import register_user
from login import login_adm_user
from menu_adm import *
from menu_user import *

id = [0]

article = 'Em um desdobramento surpreendente, Tiago, um renomado desenvolvedor de software, foi pego em flagrante ' \
          'codificando em PHP, uma linguagem de programação que ele havia criticado publicamente em várias ocasiões.'

users = {'wini1': [12345, '1'], 'wini2': [12345, '2']}
perfil_adm = {'wini1': ['Jose Winicius', 'winicius@gmail.com']}
news = {'wini1': {id[0]: ['tiago é pego codando em php', article, ['não achei que ele fosse capaz disso'], ['❤️'], '08/11/2023']}}

while True:
    print(
        '___________MENU___________\n'
        '[1]Login\n'
        '[2]Cadastrar Administrador\n'
        '[3]Cadastrar usuário\n'
        '[0]Sair'
    )
    print('_'*26)
    choice = input()
    if choice == '1':
        tipo, usuario = login_adm_user(users)
        if tipo == 1:
            menu_adm(news, id, usuario)
        elif tipo == 2:
            menu_user(news)
        else:
            print('\033[91mUsuário e senhas inválidos!\033[0m')

    elif choice == '2':
        register_adm(users, perfil_adm)

    elif choice == '3':
        register_user(users)

    elif choice == '0':
        break

    else:
        print('\033[91mOpção inválida!\033[0m')
        break
