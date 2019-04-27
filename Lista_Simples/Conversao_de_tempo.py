"""
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no 
formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
"""
#constatntes
segundosEmUmaHora   = 60 * 60
SegundosEmUmMinuto  = 60
#entradas
totalDeSengundos    = int(input())
#processos
horas               = int(totalDeSengundos / segundosEmUmaHora)
segundosRestantes   = totalDeSengundos % segundosEmUmaHora
minutos             = int(segundosRestantes / SegundosEmUmMinuto) if(segundosRestantes != 0) else 0
segundos            =  segundosRestantes % SegundosEmUmMinuto
#saídas
print(horas, ":", minutos, ":", segundos, sep="")