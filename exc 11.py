#Faça um código para ler um vetor de 30 números. Após isto, ler mais um número qualquer,
#calcular e escrever quantas vezes esse número aparece no vetor.
vetor = []
cont = 0
for x in range(30):
    n=float(input(f'Insira o {x+1}º número: '))
    vetor.append(n)
verificacao=float(input('Insira um número para verificar quantas vezes ele ocorre no vetor: '))
for n in vetor:
    if n == verificacao:
        cont +=1
print(f'O número {verificacao} aparece {cont} vezes no vetor.')
