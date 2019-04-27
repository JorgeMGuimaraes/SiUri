"""
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre 
o valor da conta a pagar.

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
"""
#constantes
tabela              = [4.00, 4.50, 5.00, 2.00, 1.50]
#entrada
codigo, quantidade  = map(int, input().split())
#processos
valorTotal          = quantidade * tabela[codigo - 1]
#saída
print("Total: R$", "{:.2f}".format(valorTotal))