"""
Leia um valor inteiro N que é o tamanho da matriz que deve ser impressa conforme o modelo fornecido.

Entrada

A entrada contém vários casos de teste e termina com EOF. Cada caso de teste é composto por um único inteiro N (3 ≤ N < 70), que 
determina o tamanho (linhas e colunas) de uma matriz que deve ser impressa.

Saída

Para cada N lido, apresente a saída conforme o exemplo fornecido.
"""
# subs
def matrizGerada(larg):
    matriz = []
    for i in range(larg):
        linha = [3] * larg
        matriz.append(linha)
    return matriz

def diagonalPrincipal(x, y):
    return y == x

def diagonalSecundaria(x, y):
    return x + y == larguraDaMatriz - 1

def operarNaMatriz(vs):
    for i in range(len(vs)):
        for j in range(len(vs)):
            if diagonalPrincipal(i, j):
                vs[i][j] = 1
            if diagonalSecundaria(i, j):
                vs[i][j] = 2
# entradas
larguraDaMatriz = input()

# processos
while larguraDaMatriz:
    larguraDaMatriz = int(larguraDaMatriz)
    matriz          = matrizGerada(larguraDaMatriz)
    operarNaMatriz(matriz)
    for i in range(larguraDaMatriz):
        for j in range(larguraDaMatriz - 1):
            print("%d"%matriz[i][j], end="")
        print("%d"%matriz[i][larguraDaMatriz - 1])
    larguraDaMatriz = input()
