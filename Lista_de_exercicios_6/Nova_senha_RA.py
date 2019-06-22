"""
Um novo conjunto de autenticação será implementado no Instituto Federal do Sul de Minas, campus Muzambinho.

Bom, o novo serviço de autenticação é seguro, sem bugs e dores de cabeça mesmo porque estamos no final de semestre. Ele permitirá que sua senha tenha espaços, mas não números ou caracteres especiais. A atualização ocorre sempre no período de férias, para que todos os ajustes sejam feitos e no final agrade todos os usuarios. Como estagiário da central de suporte da escola, seu dever é implementar a nova autenticação. Por enquanto o novo padrão para nomes de usuários está sendo estudado.



Como podemos perceber para cada conjunto de letras teremos um numero especifico. Bole um programa maroto para fazer essa conversão das letras para os números, e como você não acessará as senhas dos alunos, faça um algoritmo para que o mesmo faça o processo sozinho usando seus proprios casos de teste.

Obs : Seus casos de teste não poderão passar de 20 caracterese e a saída, 12 digitos.

Entrada
Você terá N indicando a quantidade de senhas que serão trocadas, em seguida N casos de testes.

Saída
A saída será uma lista com os novos números, criptografados das senhas que foram digitadas.
"""
# subs
def traduzir(vals):
    frase = vals.replace(" ", "")
    saida = ""
    lim = min(12, len(frase))
    for i in range(lim):
        for j in range(len(correspondencias)):
            if frase[i] in correspondencias[j]:
                saida += str(j)
    return saida

# entradas
casos = int(input())

# processos
correspondencias = ["GQaku", "ISblv", "EOYcmw", "FPZdnx", "JTeoy", "DNXfpz", "AKUgq", "CMWhr", "BLVis", "HRjt"]
saida = ""
for i in range(casos):
    print(traduzir(input()))