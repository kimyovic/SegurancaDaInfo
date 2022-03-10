print("Insira o nome do usuário")
user = str(input("Usuário: "))
print("Insira sua senha")
senha = str(input("Senha: "))

if user == senha:
    print("A senha não pode ser igual ao nome do usuário!\n")
    print("Insira o nome do usuário")
    user = str(input("Usuário: "))
    print("Insira sua senha")
    senha = str(input("Senha: "))
else:
    print("Usuario '{}' cadastrado com sucesso!".format(user))

tentativas = 0
print(user)
print("Insira sua senha")
senhaconf = input("Senha: ")
while senhaconf != senha:
        print("Senha incorreta! Tente novamente!\n")
        print("Usuário: {}".format(user))
        print("Insira sua senha")
        senhaconf = input("Senha: ")
else:
    print("\n")
    print("Usuário logado!")