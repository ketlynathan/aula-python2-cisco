from __future__ import annotations
from typing import Optional, Sequence, List, Dict, Any
from datetime import datetime, timezone
import ipaddress


class InvalidIPError(ValueError):
    """Erro lançado quando o IP for inválido."""
    pass


class Alvo:
    def __init__(self, ip: str, portas: Optional[Sequence[int]] = None) -> None:
        self._ip: Optional[str] = None
        self.ip = ip  # usa o setter (validação)
        self.portas: List[int] = list(portas or [])
        self._vulns: List[str] = []
        self.status: str = "desconhecido"
        self.criado_em: datetime = datetime.now(timezone.utc)

    # -------------------------------
    # IP (getter / setter)
    # -------------------------------
    @property
    def ip(self) -> str:
        if self._ip is None:
            raise InvalidIPError("IP não definido")
        return self._ip

    @ip.setter
    def ip(self, novo_ip: str) -> None:
        try:
            ipaddress.ip_address(novo_ip)
        except Exception as exc:
            raise InvalidIPError(f"IP inválido: {novo_ip!r}") from exc
        self._ip = novo_ip

    # -------------------------------
    # Portas
    # -------------------------------
    def adicionar_porta(self, porta: int) -> None:
        if not (1 <= porta <= 65535):
            raise ValueError("Porta deve estar entre 1 e 65535")
        if porta not in self.portas:
            self.portas.append(porta)

    def remover_porta(self, porta: int) -> None:
        if porta in self.portas:
            self.portas.remove(porta)

    # -------------------------------
    # Vulnerabilidades
    # -------------------------------
    def adicionar_vuln(self, vuln_nome: str) -> None:
        if vuln_nome not in self._vulns:
            self._vulns.append(vuln_nome)

    def get_vulns(self) -> List[str]:
        return list(self._vulns)

    # -------------------------------
    # Relatório
    # -------------------------------
    def gerar_relatorio(self) -> Dict[str, Any]:
        return {
            "ip": self.ip,
            "status": self.status,
            "portas": list(self.portas),
            "vulnerabilidades": self.get_vulns(),
            "criado_em": self.criado_em.isoformat(),
        }

    # -------------------------------
    # Representação
    # -------------------------------
    def __repr__(self) -> str:
        return (
            f"Alvo(ip={self._ip!r}, portas={self.portas!r}, "
            f"status={self.status!r})"
        )
