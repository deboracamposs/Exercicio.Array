#Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array
#diferente, após completar a digitação, imprimir , nome, senha e posição dos dados no array
usuarios= []
senhas=[]
for x in range(5):
    nome=input(f'Digite o usuário {x+1}: ')
    senha=input(f'Digite a senha {x+1}: ')
    usuarios.append(nome)
    senhas.append(senha)
for i in range(5):
    print(' Esses são os dados dos usuários: ')
    print(f' Nome: {usuarios[i]}\n Senha: {senhas[i]}\n Posição: {i} ')