"""
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você 
deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma 
linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.
"""
# subs
def quantidadeDeCasos():
    return int(input())

def quantidadeDeInpares(num1, num2):
    soma = 0
    if num1 == num2:
        return "0"
    if num2 < num1:
        num1, num2 = num2, num1
    for i in range(num1 + 1, num2):
        if i % 2 != 0:
            soma += i
    return str(soma)

# entradas
casos = quantidadeDeCasos()
# processos
for i in range(casos):
    x, y = map(int, input().split())
    print(quantidadeDeInpares(x, y))


