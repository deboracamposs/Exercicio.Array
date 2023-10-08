#Ler um vetor A de 10 números. logo em seguida, ler mais um número e guardar em uma variável X. Armazenar em um vetor M o resultado de
#cada elemento de A multiplicado pelo valor X. Logo após, imprimir o vetor M.
a = []
for i in range(10):
    num=float(input(f'Digite o {i+1}º número:'))
    a.append(num)
x = float(input('Digite o valor de X: '))
m = [num * x for num in a]
print('Resultados abaixo:')
for num in m:
    print(f'Os números na lista são: {a} \n Multiplicados por {x} \n Resultam em: {m}')
    break