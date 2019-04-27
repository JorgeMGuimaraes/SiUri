"""
Bem-vindos e bem-vindas à Escola de Inverno da Maratona de Programação 2015 de Erechim! Esperamos sinceramente que vocês aprendam muito 
nestes dias para que tenham muito sucesso nas competições de Programação ainda por vir, mas sobretudo esperamos que vocês curtam a 
Escola, pois quando nos divertimos e temos prazer em estudar e programar, o treino deixa de ser um fardo e se torna um hobby. Então, 
divirtam-se!

O inverno é uma estação maravilhosa, não é mesmo? Todos nós amamos vestir um poncho, participar de uma roda de chimarrão, assar pinhões 
no fogão a lenha… Mas nem todos gostam do inverno, especialmente em lugares onde o inverno costuma ser muito cruel. Em Westeros, por 
exemplo, o humor das pessoas é definido de acordo com as tendências climáticas. Com base nas temperaturas dos três últimos dias, as 
pessoas podem ficar tristes ou felizes, ficando mais propensas a fazer guerra ou fazer amor, respectivamente. E, sejamos sinceros, é 
justamente por causa das cenas de amor e de guerra que amamos Game of Thrones!





Entrada
A entrada consiste apenas de três inteiros, A, B e C (-100 ≤ A, B, C ≤ 100), os quais representam respectivamente as temperaturas registradas no 1º, no 2º e no 3º dias.

Saída
Imprima uma linha contendo uma carinha feliz ou triste, representando como fica o humor do povo de Westeros de acordo com as tendências climáticas.

"""
#constantes
FELIZ   = ":)"
TRISTE  = ":("
#entradas
dia1, dia2, dia3 = map(int, input().split())
#processos
carinha = ""
# Se a temperatura desceu do 1º para o 2º dia,
if dia1 > dia2:
    # mas subiu ou permaneceu constante do 2º para o 3º, as pessoas ficam felizes 
    if dia2 <= dia3: carinha = FELIZ
    # e do 2º para o 3º
    else:
        # mas desceu do 2º para o 3º menos do que descera do 1º para o 2º, as  pessoas ficam felizes.
        if dia1 - dia2 > dia2 - dia3: carinha       = FELIZ
        # mas desceu do 2º para o 3º no mínimo o tanto que descera do 1º para o 2º, as pessoas ficam tristes
        elif dia1 - dia2 <= dia2 - dia3: carinha    = TRISTE
# Se a temperatura subiu do 1º para o 2º dia
elif dia1 < dia2:
    # mas desceu ou permaneceu constante do 2º para o 3º, as pessoas ficam tristes 
    if dia2 >= dia3: carinha = TRISTE
    # e do 2º para o 3º,    
    elif dia2 < dia3:
        # mas subiu do 2º para o 3º menos do que subira do 1º para o 2º, as pessoas ficam tristes (terceira figura).
        if dia2 - dia1 > dia3 - dia2: carinha       = TRISTE
        # mas subiu do 2º para o 3º no mínimo o tanto que subira do 1º para o 2º, as pessoas ficam felizes
        elif dia2 - dia1 <= dia3 - dia2: carinha    = FELIZ
# Se a temperatura permaneceu constante do 1º para o 2º dia,
else:
    # as pessoas ficam felizes se subiu do 2º para o 3º dia
    if dia2 < dia3: carinha = FELIZ
    # ou tristes caso contrário
    else: carinha = TRISTE

#saidas
print(carinha)