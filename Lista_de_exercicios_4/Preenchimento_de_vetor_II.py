"""
Faça um programa que leia um valor T e preencha um vetor N[1000] com a sequência de valores de 0 até T-1 repetidas vezes, conforme 
exemplo abaixo. Imprima o vetor N.

Entrada
A entrada contém um valor inteiro T (2 ≤ T ≤ 50).

Saída
Para cada posição do vetor, escreva "N[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.
"""
#constantes
maxIteracoes = 1000
#entradas
t = int(input())
#processos
n = [0] * maxIteracoes
for i in range(maxIteracoes):
    n[i] = i % t
    print("N[%d] = %d"%(i, n[i]))