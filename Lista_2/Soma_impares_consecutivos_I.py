"""
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na 
entrada que deverá caber em um inteiro.
"""
#entradas
A1 = int(input())
An = int(input())
#processos
if A1 > An:
    A1, An = An, A1
A1 += 1 if A1 % 2 == 0 else 2
An -= 1 if An % 2 == 0 else 2
n = 1 + (An - A1) / 2
somaDosTermosDaPA = int((A1 + An) * n / 2)
#saídas
print(somaDosTermosDaPA)