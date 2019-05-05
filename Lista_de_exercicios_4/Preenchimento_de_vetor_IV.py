"""
Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só que o tamanho 
de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e 
utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em cada 
um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for 
necessário.
Entrada

A entrada contém 15 números inteiros.

Saída

Imprima a saída conforme o exemplo abaixo.

"""
# consts
pares               = []
impares             = []
totalDeIteracoes    = 15
# entradas

# processos
for i in range(totalDeIteracoes):
    entrada = int(input())
    if entrada % 2 == 0:
        pares.append(entrada)
        if len(pares) == 5:
            for i in range(len(pares)):
                print("par[%d] = %d"%(i, pares[i]))
            pares.clear()
    else:
        impares.append(entrada)
        if len(impares) == 5:
            for i in range(len(impares)):
                print("impar[%d] = %d"%(i, impares[i]))
            impares.clear()
for i in range(len(impares)):
    print("impar[%d] = %d"%(i, impares[i]))
for i in range(len(pares)):
    print("par[%d] = %d"%(i, pares[i]))
