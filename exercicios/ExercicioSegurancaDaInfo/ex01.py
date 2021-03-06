import re
print("Cadastre o nome do usuário")
user = str(input("Usuário: "))
def senhaValida(senha):
    min_number = 1
    min_upper_char = 1
    min_lower_char = 1
    min_len = 8
    max_len = 10
    if len(senha) < min_len:
        print("A senha precisa ter no mínimo {} caracteres!".format(min_len))
    if len(senha) > max_len:
        print("A senha não pode ter mais que {} caracteres!".format(max_len))
    if len(re.findall(r"[A-Z]", senha)) < min_upper_char:
        print("A senha precisa conter carcteres maiúsculos!")
    if len(re.findall(r"[a-z]", senha)) < min_lower_char:
        print("A senha precisa conter carcteres minúsculos!")
    if len(re.findall(r"[0-9]", senha)) < min_number:
        print("A senha precisa conter ao menos {}!".format(min_number))
    else:
        print("Senha cadastrada!")
print("Cadastre sua senha")
print("A senha precisa conter 10 caracteres: letras maiúsculas, minusculas e números")
senha = str(input("Senha: "))
while senhaValida(senha):
    print("A senha não cumpre os requisitos, por favor tente novamente!")
    print("Cadastre sua senha")
    print("A senha precisa conter 10 caracteres: letras maiúsculas, minusculas e números")
    senha = str(input("Senha: "))
else:
if user == senha:
        print("A senha não pode ser igual ao nome do usuário!\n")
        print("Insira o nome do usuário")
        user = str(input("Usuário: "))
        print("Insira sua senha")
        senha = str(input("Senha: "))
else:
    while senhaValida(senha):
        print("A senha não cumpre os requisitos, por favor tente novamente!")
        print("Cadastre sua senha")
        print("A senha precisa conter 10 caracteres: letras maiúsculas, minusculas e números")
        senha = str(input("Senha: "))
tentativas = 0
print("\n Usuário - {}".format(user))
print("Insira sua senha")
senhaconf = input("Senha: ")
while senhaconf != senha:
    print("Senha incorreta! Tente novamente!\n")
    print("Usuário: {}".format(user))
    print("Insira sua senha")
    senhaconf = input("Senha: ")
    if tentativas < 5:
        print("{} tentativas".format(tentativas + 1))
        tentativas += 1
    else:
        print("Usuário Bloqueado!")
        break
else:
    print("\n")
    print("Usuário logado!")