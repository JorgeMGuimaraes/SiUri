"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em 
seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
"""
#input
A, B, C     = map(int, input().split())
#processos
valores     = [A, B, C]
ordenados   = [A, B, C]
ordenados.sort()
    #print ordenados
for valor in ordenados:
    print(valor)
print()
    #print valores originais
for valor in valores:
    print(valor)