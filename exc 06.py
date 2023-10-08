#Faça um código para ler 5 números e armazenar em um vetor. Após a leitura total dos 5 números, o código deve
#escrever esses 5 números lidos na ordem inversa
vetor = []
for x in range(5):
    num=float(input(f'Digite o {x+1}º número: '))
    vetor.append(num)
print('Números na ordem inversa:')
for i in range (4,-1,-1):
    print(vetor[i])