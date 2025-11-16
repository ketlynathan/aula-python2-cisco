from __future__ import annotations
from typing import List, Sequence
from src.scanners.base import Scanner
from src.models.alvo import Alvo


class PortScanner(Scanner):
    def __init__(self, alvo: Alvo, portas_a_testar: Sequence[int] | None = None):
        super().__init__(alvo, ferramenta_nome="PortScanner (simulado)", timeout=30)
        self.portas_a_testar: List[int] = list(
            portas_a_testar or alvo.portas or [])


def scan_portas(self) -> List[int]:
    portas_abertas = [p for p in self.portas_a_testar if 0 < p < 65536]
    for p in portas_abertas:
        if p not in self.alvo.portas:
            self.alvo.adicionar_porta(p)
        return portas_abertas


def executar_scan(self) -> bool:
    online = super().executar_scan()
    if online:
        portas = self.scan_portas()
    if 22 in portas:
        self.alvo.adicionar_vuln("ssh_config_inseguro")
    return online
