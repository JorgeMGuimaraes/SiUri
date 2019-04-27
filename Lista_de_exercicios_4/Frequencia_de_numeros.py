"""
Neste problema sua tarefa será ler vários números e em seguida dizer quantas vezes cada número aparece na entrada de dados, ou seja, 
deve-se escrever cada um dos valores distintos que aparecem na entrada por ordem crescente de valor.

Entrada
A entrada contém apenas 1 caso de teste. A primeira linha de entrada contem um único inteiro N, que indica a quantidade de valores que 
serão lidos para X (1 ≤ X ≤ 2000) logo em seguida. Com certeza cada número não aparecerá mais do que 20 vezes na entrada de dados.

Saída
Imprima a saída de acordo com o exemplo fornecido abaixo, indicando quantas vezes cada um deles aparece na entrada por ordem crescente 
de valor.
"""
#subs
def IncrementarLista(lista, valor):
        for item in lista:
                if item[0] == valor:
                        item[1] += 1
                        return None
        lista.append([valor, 1])
        return None
#entradas
totalDeCasos = int(input())
#processos
valoresComputados = [[int(input()), 1]]
for i in range(1, totalDeCasos):
        caso = int(input())
        IncrementarLista(valoresComputados, caso)
valoresComputados.sort()
#saidas
for valor in valoresComputados:
        print("%d aparece %d vez(es)"%(valor[0], valor[1]))