def register_user(users):
    name = input('Nome:')
    email = input('Informe seu email:')
    while True:
        usuario = input('Crie um usuário:')
        if usuario not in users:
            password = int(input('Crie uma senha:'))
            if len(str(password)) > 4:
                users[usuario] = [password, '2']
                print('\033[92mCadastro concluído.\033[0m')
                break
            else:
                print('\033[91mSenha deve ter pelo menos 4 dígitos!\033[0m')
        else:
            print('\033[91mUsuário em uso. Tente outro!\033[0m')
