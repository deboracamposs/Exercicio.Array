#Altere o exercício anterior para permitir achar o nome de um aluno na lista
qtd=int(input("Quantos alunos tem na sala?"))
nomealunos = [0]*qtd
achou = 0
for x in range (qtd):
    nomealunos[x]=input('Digite o nome dos aluno:')
perg=input('Qual aluno deseja localizar?')
for i in range(qtd):
    if perg == nomealunos[i]:
        achou=achou+1
        print(f'O aluno {nomealunos[i]}, está na posição {i}.', end=" ")
if achou ==  0:
        print(f'O nome {perg} não está na lista')