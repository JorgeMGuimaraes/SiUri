"""
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” 
"""
#subs

#entradas
horaInicio, minutoInicio, horaFim, minutoFim = map(int, input().split())
#processos
if horaFim <= horaInicio:
    if minutoFim <= minutoInicio:
        horaFim     += 24
if minutoFim < minutoInicio:
    horaFim     -= 1
    minutoFim   += 60
minutos = minutoFim - minutoInicio
horas   = horaFim - horaInicio
#saidas
print("O JOGO DUROU", horas, "HORA(S) E", minutos, "MINUTO(S)")