"""


Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a 
soma ou a média considerando somente aqueles elementos que estão na área direita da matriz, conforme ilustrado abaixo (área verde).

Entrada

A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá 
ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

Saída

Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.
"""
# constantes
larguraDaMatriz = 12
# subs
def matrizGerada():
    matriz = []
    for i in range(larguraDaMatriz):
        linha = [0.0] * larguraDaMatriz
        for j in range(larguraDaMatriz):
            linha[j] = float(input())
        matriz.append(linha)
    return matriz

def acimaDaDiagonalPrincipal(x, y):
    return y > x

def abaixoDaDiagonalPrincipal(x, y):
    return y < x

def acimaDaDiagonalSecundaria(x, y):
    return x + y < larguraDaMatriz - 1

def abaixoDaDiagonalSecundaria(x, y):
    return x + y > larguraDaMatriz - 1

def calculaSomaOuMedia(vs, tipo):
    soma            = 0
    divisorDaMedia  = 0
    for i in range(len(vs[0])):
        for j in range(len(vs[0])):
            if acimaDaDiagonalPrincipal(i, j) and abaixoDaDiagonalSecundaria(i, j):
                soma            += vs[i][j]
                divisorDaMedia  += 1
    return soma if tipo == "S" else soma / divisorDaMedia

# entradas
tipoDeOperacao  = input()
# processos
total           = calculaSomaOuMedia(matrizGerada(), tipoDeOperacao)
#saidas
print("{:.1f}".format(total))