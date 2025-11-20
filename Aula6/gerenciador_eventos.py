import os
import json
from datetime import datetime


def configurar_ambiente():
    pasta_dados = "dados"
    os.makedirs(pasta_dados, exist_ok=True)
    return os.path.join(pasta_dados, "eventos.json")


def carregar_eventos(caminho_arquivo):
    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except (json.JSONDecodeError, IOError):
            print("Erro ao carregar os eventos. Iniciando com uma lista vazia.")
            return []
    return []


def salvar_eventos(caminho_arquivo, eventos):
    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(eventos, arquivo, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao salvar os eventos: {e}")


def adicionar_evento(eventos):
    titulo = input("Digite o título do evento: ").strip()
    if not titulo:
        print("O título do evento não pode ser vazio.")
        return

    while True:
        try:
            data_hora_str = input(
                "Digite a data e hora do evento (formato: DD/MM/AAAA HH:MM): "
            ).strip()
            datetime_obj = datetime.strptime(data_hora_str, "%d/%m/%Y %H:%M")
            break
        except ValueError:
            print("Formato inválido. Tente novamente.")

    eventos.append(
        {"titulo": titulo, "data_hora": datetime_obj.isoformat()}
    )
    print(f"Evento '{titulo}' adicionado com sucesso.")


def listar_eventos(eventos):
    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    eventos_ordenados = sorted(eventos, key=lambda e: e["data_hora"])
    agora = datetime.now()

    print("\n📋 Eventos cadastrados:\n")
    for i, evento in enumerate(eventos_ordenados, start=1):
        data_hora = datetime.fromisoformat(evento["data_hora"])
        status = "[Passado]" if data_hora < agora else "[Futuro]"
        print(
            f"{i}. {evento['titulo']} - {data_hora.strftime('%d/%m/%Y %H:%M')} {status}")
        print("-" * 40)


def menu_principal():
    caminho_arquivo = configurar_ambiente()
    eventos = carregar_eventos(caminho_arquivo)

    while True:
        print("\n" + "="*50)
        print("📅 GERENCIADOR DE EVENTOS")
        print("="*50)
        print("1️⃣  Adicionar evento")
        print("2️⃣  Listar eventos")
        print("3️⃣  Sair")
        print("="*50)

        opcao = input("\n👉 Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_evento(eventos)
            salvar_eventos(caminho_arquivo, eventos)

        elif opcao == "2":
            listar_eventos(eventos)

        elif opcao == "3":
            print("\n👋 Até logo!\n")
            break

        else:
            print("❌ Opção inválida! Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    menu_principal()
