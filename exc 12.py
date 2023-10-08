#Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes, e que exiba a lista desses nomes na tela.
#Após exibir essa lista, o programa deve mostrar também os nomes na ordem inversa em que o usuário os digitou, um por linha.
nomes=[]
for x in range(5):
    nome=input(f'Insira o {x+1}º nome aqui: ').upper()
    nomes.append(nome)
print("\nNomes na ordem inversa:")
for nome in reversed(nomes):
    print(nome)
