"""
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:


Salário	Percentual de Reajuste
0 - 400.00          15%
400.01 - 800.00     12%
800.01 - 1200.00    10%
1200.01 - 2000.00    7%
Acima de 2000.00     4%
Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em 
percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme exemplo abaixo.
Novo salario: 460.00
Reajuste ganho: 60.00
Em percentual: 15 %
"""
#Constantes
tabelaDeReajustes   = [[400.0, 0.15], [800.0, 0.12], [1200.0, 0.10], [2000.0, 0.07]]
maxReajuste         = 0.04
#Subs
def encontrarReajuste(salarioBase):
    for relacao in tabelaDeReajustes:
        if salarioBase <= relacao[0]:
            return relacao[1]
    return maxReajuste
#Entradas
entradaSalario     = float(input())
indiceDeReajuste   = encontrarReajuste(entradaSalario)
valorReajuste      = entradaSalario * indiceDeReajuste
#Output
print("Novo salario:", "{:.2f}".format(entradaSalario + valorReajuste))
print("Reajuste ganho:", "{:.2f}".format(valorReajuste))
print("Em percentual:", str(int(indiceDeReajuste * 100)), "%")