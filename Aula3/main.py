# Slice

alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("d" in alfabeto)

# procurar um numero
print("2" in alfabeto)

# procurar um trecho
print("yZa" in alfabeto)

# procurar vogais no alfabeto
vogais = "aeiouAEIOU"
for letra in vogais:
    if letra not in alfabeto:
        print(letra, end="")
        # print(f"A letra {letra} está no alfabeto")
    # else:
        # print(f"A letra {letra} não está no alfabeto")


# Transformar caractere da string em maiusculo
nome = "pEDro sAmpaiO"
print(nome.capitalize())
