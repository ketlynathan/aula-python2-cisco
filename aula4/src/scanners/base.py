"""
Scanner base: define contrato e comportamentos básicos.
"""
from __future__ import annotations
from typing import Dict, Any
from src.models.alvo import Alvo


class Scanner:
    def __init__(self, alvo: Alvo, ferramenta_nome: str = "Scanner Base", timeout: int = 60) -> None:
        self.alvo = alvo
        self.ferramenta_nome = ferramenta_nome
        self.timeout = timeout


def executar_scan(self) -> bool:
    is_online = bool(self.alvo.portas)
    self.alvo.status = "online" if is_online else "offline"
    return is_online


def gerar_report(self) -> Dict[str, Any]:

    base = self.alvo.gerar_relatorio()
    base.update({"scanner": self.ferramenta_nome, "timeout": self.timeout})
    return base
