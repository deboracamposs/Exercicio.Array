#Altere o sistema anterior e faça um sistema de login, pedindo a senha do usuário e mostrando seu nome
# e a mensagem, login efetuado com sucesso.
senhas_usuarios = {}
for x in range(5):
    nome=input(f'Digite o usuário {x+1}: ')
    senha=input(f'Digite a senha {nome}: ')
    senhas_usuarios[nome]=senha

login_nome=input('Digite seu usuário: ')
login_senha=input('Digite sua senha: ')

if login_nome in senhas_usuarios and senhas_usuarios[login_nome] == login_senha:
    print(f'Login efetuado com sucesso, {login_nome} ! ')
else:
    print('Usuário ou senha incorretos.')
