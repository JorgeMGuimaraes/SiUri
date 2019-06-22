"""
Dodô, Leo e Pepper passam várias madrugadas conversando, em algum lugar do Condomínio Jardim Botânico IV. Diversos assuntos astrais ganham pauta nestas conversas homéricas. Nas últimas sessões, Dodô tem falado do jogo de RPG que ele e Leo estão inventando, Leo (para “variar”, mas com razão) tem falado do gênero musical heavy metal e Pepper ficou fascinado com a história da mitologia grega contada por Leo.

Os garotos resolveram adotar uma estratégia para dividir as sessões igualmente entre os assuntos, de modo que eles possam especular cada um ao máximo e chegarem a conclusões astronômicas. Eles irão jogar “pedra, papel e tesoura” para decidir o assunto da sessão de hoje, e então irão alternar os assuntos nas próximas sessões. Dadas as jogadas de Dodô, Leo e Pepper, nesta ordem, você deve determinar o assunto da sessão de hoje.

Entrada
A entrada é composta por vários casos de teste e termina com fim de arquivo. Cada caso de teste é composto por uma única linha, que contém as jogadas de cada um dos garotos, como mostrado nos exemplos.

Saída
Para cada caso de teste, imprima uma única linha com a mensagem "Os atributos dos monstros vao ser inteligencia, sabedoria..." para indicar que Dodô é o vencedor, a mensagem "Iron Maiden’s gonna get you, no matter how far!" para indicar que Leo é o vencedor, a mensagem "Urano perdeu algo muito precioso..." para indicar que Pepper é o vencedor, ou a mensagem "Putz vei, o Leo ta demorando muito pra jogar..." se houver empate.
"""
# subs
def pedraVence(vals):
    if "pedra" in vals:
        return vals.count("tesoura") == 2

def papelVence(vals):
    if "papel" in vals:
        return vals.count("pedra") == 2

def tesouraVence(vals):
    if "tesoura" in vals:
        return vals.count("papel") == 2


# Main
respostas   = ["Os atributos dos monstros vao ser inteligencia, sabedoria...", "Iron Maiden's gonna get you, no matter how far!", "Urano perdeu algo muito precioso...", "Putz vei, o Leo ta demorando muito pra jogar..."]
entrada     = input()
try:
    while entrada:
        jogadas = list(entrada.split())
        if pedraVence(jogadas):
            print(respostas[jogadas.index("pedra")])
        elif papelVence(jogadas):
            print(respostas[jogadas.index("papel")])
        elif tesouraVence(jogadas):
            print(respostas[jogadas.index("tesoura")])
        else:
            print(respostas[3])
        entrada = input()
except:
    pass
