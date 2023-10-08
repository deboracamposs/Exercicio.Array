#Perguntar ao usuário quantos alunos tem na sala e criar um array, unidimensional(Vetor) com o nome de todos os alunos da sala
qtd=int(input("Quantos alunos tem na sala?"))
nomealunos = [0]*qtd
for x in range (qtd):
    nomealunos[x]=input('Digite o nome dos aluno:')
for i in range(qtd):
    print(nomealunos[i] , end = " ")