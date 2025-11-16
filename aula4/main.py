"""Ponto de entrada simples - orquestra e imprime relatórios em JSON."""
import json
from src.models.alvo import Alvo
from src.scanners.port_scanner import PortScanner
from src.scanners.vuln_scanner import VulnScanner


def main() -> None:
    alvo1 = Alvo("192.168.10.10", portas=[80, 443, 22])
    alvo2 = Alvo("192.168.10.11", portas=[8080])

    ps = PortScanner(alvo1)
    vs = VulnScanner(alvo2, scripts=["smb_vuln", "http_vuln"])

    ps.executar_scan()
    vs.executar_scan()

    rel1 = ps.gerar_report()
    rel2 = vs.gerar_report()

    print(json.dumps(rel1, indent=2, ensure_ascii=False))
    print(json.dumps(rel2, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
