#Faça um algoritmo que leia 30 valores do tipo inteiro e armazene-os em um vetor. A seguir, o algoritmo deverá informar
#(1) todos os números pares que existem no vetor; (2) o menor e o maior valor existente no vetor;
#(3) quantos dos valores do vetor são maiores que a média desses valores:
vetor=[]
for x in range(30):
    valor=int(input(f'Insira o {x+1}º valor inteiro: '))
    vetor.append(valor)
mn_valor=vetor[0]
ma_valor=vetor[0]
soma = sum(vetor)
media = soma/30
valor_maior_que_media=[]
for valor in vetor:
     if valor % 2 ==0:
         print(f'O número par:{valor}')

     if valor < mn_valor:
         mn_valor = valor

     if valor > ma_valor:
         ma_valor = valor

     if valor > media:
         valor_maior_que_media.append(valor)

print(f'Menor valor: {mn_valor}')
print(f'Maior valor: {ma_valor}')
print(f'Valores maiores que a média: {valor_maior_que_media}')
