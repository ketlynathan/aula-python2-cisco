import math

# A função de cálculo do empréstimo


def calcular_prestacao(P, i, n):
    """
    Calcula a prestação mensal de um empréstimo (Fórmula de Juros Compostos).
    P: Principal (Valor do Empréstimo)
    i: Taxa de Juros Mensal (em decimal)
    n: Parcelas - Número do Período
    """
    if i == 0:
        return P / n

    # M = P * (i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)
    # A variável 'math' foi importada e existe apenas neste namespace

    prestacao = P * (i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)
    return round(prestacao, 2)
