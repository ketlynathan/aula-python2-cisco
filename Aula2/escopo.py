# Escopo Global

idade = 42


def fontedajuventude(idade=idade):
    idade -= 10  # Escopo local
    print("Idade dentro da função:", idade)


print("Idade fora da função:", idade)
fontedajuventude()
print("Idade fora da função após a chamada:", idade)
