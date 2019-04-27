"""
Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do 
programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.
"""
#subs

#entrada
linhas = int(input())
#processos
for i in range(1, (linhas * 4) + 1):
    if i % 4 == 0:
        print("PUM", end = "\n")
    else:
        print(i, end = " ")