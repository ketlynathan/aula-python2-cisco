# LOBBY (Global Scope)
nome_sindico = "Sr. Silva"


def apartamento_301():
    # --> Este é o ESCOPO ENCLOSING (Envolvente)

    # Armário no Apartamento (Enclosing)
    nome_morador = "Ana"

    def suite_master():
        # --> Este é o ESCOPO LOCAL

        # Armário na Suíte (Local)
        nome_visitante = "Carlos"

        # 1. Tentando acessar o nome do visitante:
        #    Procura no Local (Suíte) -> ACHA!
        print(f"Na suíte está: {nome_visitante}")

        # 2. Tentando acessar o nome do morador:
        #    Procura no Local (Suíte) -> Não acha.
        #    Procura no Enclosing (Apartamento) -> ACHA!
        print(f"O morador do apartamento é: {nome_morador}")

        # 3. Tentando acessar o nome do síndico:
        #    Procura no Local (Suíte) -> Não acha.
        #    Procura no Enclosing (Apartamento) -> Não acha.
        #    Procura no Global (Lobby) -> ACHA!
        print(f"O síndico do prédio é: {nome_sindico}")

    # Fim da Suíte

    # O apartamento "chama" a função da suíte
    suite_master()

# Fim do Apartamento


# "Entramos" no apartamento para começar
apartamento_301()
