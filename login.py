#essa def está responsável pelo login dos usuários/adms
#tipo = 1(adm), tipo = 2(usuário) e tipo = 0(nada)
def login_adm_user(users):
    tipo = 0
    usuario = input('Usuário:')
    password = int(input('Senha:'))
    if usuario in users and password == users[usuario][0]:
        if users[usuario][1] == '1':
            tipo = 1
        else:
            tipo = 2

    return tipo, usuario
