class Alvo:
    def __init__(self, ip, portas):
        self._ip = ip
        self.portas = portas
        self.status = "desconhecido"
        self._vulns = []

    def get_ip(self):
        print("acessando o nosso IP...")
        return self._ip

    def set_ip(self, novo_ip):
        print("Validando o IP...")
        if "." in novo_ip and len(novo_ip) > 7:
            self._ip = novo_ip
        else:
            print(f"Erro: {novo_ip} não parece um IP válido.")

    def _scan_interno(self):
        self._vulns.append("SQLI")
        self.status = "online"

    def scan(self):
        print(f"Iniciando scan em {self.get_ip()} nas portas {self.portas}...")
        self._scan_interno()
        print("scan concluido")

    def report(self):
        print(f"--- Relatório do IP: {self.get_ip()} ---")
        print(f"Status: {self.status}")
        print(f"Portas: {self.portas}")
        print("Vulnerabilidades encontradas:")

        if self._vulns:
            for vuln in self._vulns:
                print(f"  - {vuln}")
        else:
            print("  Nenhuma")

        print("--- Fim do Relatório ---")
        print()


print("Criando alvos...\n")

alvo1 = Alvo("192.168.10.10", [80, 443, 22])
alvo2 = Alvo("192.168.10.11", [8080])

print(f"IP do Alvo 1: {alvo1.get_ip()}")
print(f"IP do Alvo 2: {alvo2.get_ip()}")

print("\nExecutando ações...\n")
alvo1.scan()
alvo2.scan()

print("\nGerando relatórios...\n")
alvo1.report()
alvo2.report()
