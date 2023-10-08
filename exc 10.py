#Faça um código para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois vetores A e B (de tamanho N cada um) e depois
#armazenar em um terceiro vetor Soma a soma dos elementos do vetor A com os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma.
n = int(input('Digite o tamanho dos vetores: '))
a = []
b = []
soma = []
print('Os elementos do vetor A:')
for x in range(n):
    elemento=int(input(f'Insira o elemento {x+1}º de A:'))
    a.append(elemento)
print('Os elementos do vetor B:')
for y in range(n):
    elemento=int(input(f'Insira o elemento {y+1}º de B:'))
    b.append(elemento)

for z in range(n):
    soma_dos_elementos=a[z]+b[z]
    soma.append(soma_dos_elementos)
print('A soma dos vetores A e B são:')
print(soma)