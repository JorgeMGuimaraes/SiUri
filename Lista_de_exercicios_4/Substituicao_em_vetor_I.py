"""
Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o 
vetor X.

Entrada
A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.

Saída
Para cada posição do vetor, escreva "X[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.
"""
#constantes
x = [0] * 10
#processos
for i in range(10):
    entrada = int(input()) 
    x[i]    = entrada if entrada > 0 else 1
    print("X[%d] = %d"%(i, x[i]))