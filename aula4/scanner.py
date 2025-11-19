alvo_ip = "192.168.10.10"
alvo_porta = [80, 443, 22]
alvo_tatus = "online"

alvo2_ip = "192.168.10.11"
alvo2_porta = [8080]
alvo2_tatus = "online"


def scan_alvo(ip, porta):
    print(f"Escaneando o alvo {ip} que está {porta}")
    return True


def gerar_report(ip, status):
    print(f"Gerando relatório para o alvo {ip} que está {status}")


scan_alvo(alvo_ip, alvo_porta)
gerar_report(alvo_ip, alvo_tatus)
