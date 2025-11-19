# Emprestimos

import math

# --- Função de calculo (Inalterada) ---

# Define a função que calcula o valor da prestação (Fórmula price).


def calcular_prestacao(p, i, n):
    """
    Calcula o valor da prestação mensal de um empréstimo (tabela Price).

    Argumentos:
    p (float): Valor principal do empréstimo.
    i (float): Taxa de juros mensal (em decimal).
    n (int): Número de parcelas.

    Retorna:
    float: Valor da prestação mensal.
    """
    # Se a taxa de juros for zero, o cálculo é uma simples divisão
    if i == 0:
        prestacao_simples = p / n
        return prestacao_simples

    # Cálculo da prestação usando a fórmula Price
    else:
        # Fórmula: M = P * [ (i * (1 + i)^n] / ((1 + i)^n – 1) ]

        # Para facilitar a leitura, calculamos a parte (1+i)^n separadamente
        termo_composto = math.pow((1 + i), n)

        # Aplica a fórmula completa
        prestacao_composta = p * ((i * termo_composto) / (termo_composto - 1))

        # Retorna o valor calculado
        return prestacao_composta


# p - Valor principal (Quanto quero de emprestimo)
p_str = input("Digite o valor do emprestimo:(ex:10.000) ")
p_str_limpo = p_str.replace(".", "")
p_str_python = p_str_limpo.replace(",", ".")
p = float(p_str_python)

# i - Taxa de juros
i_str = input("Digite a taxa de juros (ex: 5 para 5%): ")
i_str_python = i_str.replace(",", ".")
i = float(i_str_python)

# Se for digitado 5, converte para 0.05 automaticamente
if i > 1:
    i = i / 100


# n - Numero de meses (inteiro não precisa de tratamento especial)
n = int(input("Digite o némero de parcelas:"))


# --- Execução principal (Inalterada) ---

# Chama a função e armazena o resultado
valor_parcela = calcular_prestacao(p, i, n)

# Exibe o resultado formatado com 2 casas decimais
print(f"O valor da parcela mensal é: R$ {valor_parcela:.2f}")
