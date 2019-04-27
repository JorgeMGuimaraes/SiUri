"""
Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que 
a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever 
"Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores.
"""
#entradas
A, B, C, D = map(int, input().split())
#processos
condicao1 = B > C
condicao2 = D > A
condicao3 = (C + D) > (A + B)
condicao4 = C > 0 and D > 0
condicao5 = A % 2 == 0
#saída
msg = "Valores aceitos" if( condicao1 and condicao2 and condicao3 and condicao4 and condicao5) else "Valores nao aceitos"
print(msg)