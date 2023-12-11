def register_adm(users, perfil_adm):
    name = input('Nome:')
    email = input('E-mail:')
    cpf = int(input('CPF:'))
    if len(str(cpf)) == 11:
        while True:
            usuario = input('Crie um usuário:')
            if usuario not in users:
                password = int(input('Crie uma senha:'))
                if len(str(password)) >= 4:
                    users[usuario] = [password, '1']
                    perfil_adm[usuario] = [name, email]
                    print('\033[92mCadastro Concluído.\033[0m')
                    break
                else:
                    print('\033[91mSenha deve ter pelo menos 4 dígitos!\033[0m')
            else:
                print('\033[91mUsuário em uso. Tente outro!\033[0m')
    else:
        print('\033[91mCPF inválido.\033[0m')
