#Altere o exercício anterior e mostre na tela, ao final, o nome de cada aluno e sua respectiva posiçãoqtd=int(input("Quantos alunos tem na sala?"))
qtd=int(input("Quantos alunos tem na sala?"))
nomealunos = [0]*qtd
for x in range (qtd):
    nomealunos[x]=input('Digite o nome dos aluno:')
for i in range(qtd):
    print(nomealunos[i], i , end = " ")