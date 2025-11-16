from __future__ import annotations
from typing import List, Sequence
from src.scanners.base import Scanner
from src.models.alvo import Alvo


class VulnScanner(Scanner):
    def __init__(self, alvo: Alvo, scripts: Sequence[str] | None = None):
        super().__init__(alvo, ferramenta_nome="VulnScanner (simulado)", timeout=300)
        self.scripts: List[str] = list(scripts or [])


def executar_scan_vuln(self) -> List[str]:
    encontrados: List[str] = []
    for s in self.scripts:
        encontrados.append(f"{s}_detectado")
        self.alvo.adicionar_vuln(f"{s}_detectado")
    if encontrados:
        self.alvo.status = "vulneravel"
    return encontrados


def executar_scan(self) -> bool:
    online = super().executar_scan()
    if online:
        self.executar_scan_vuln()
    return online
