"""
Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido. Lembre que os 2 primeiros 
elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele. Todos os valores de Fibonacci 
calculados neste problema devem caber em um inteiro de 64 bits sem sinal.

Entrada
A primeira linha da entrada contém um inteiro T, indicando o número de casos de teste. Cada caso de teste contém um único inteiro 
N (0 ≤ N ≤ 60), correspondente ao N-esimo termo da série de Fibonacci.

Saída
Para cada caso de teste da entrada, imprima a mensagem "Fib(N) = X", onde X é o N-ésimo termo da série de Fibonacci.
"""
#constantes
totalDeCasos = 61
#entradas
casosDeTeste        = int(input())
#processos
serieDeFibonacci    = [0] * totalDeCasos
serieDeFibonacci[0] = 0
serieDeFibonacci[1] = 1
for i in range(2, totalDeCasos):
        serieDeFibonacci[i] = serieDeFibonacci[i - 1] + serieDeFibonacci[i -2]

for i in range(casosDeTeste):
    caso = int(input())
    print("Fib(%d) = %d" %(caso, serieDeFibonacci[caso]))