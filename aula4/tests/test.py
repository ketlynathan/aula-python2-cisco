# tests/test_main.py
import pytest
from main import Alvo, PortScanner, VulnScanner
from datetime import datetime, UTC


def test_alvo_criacao():
    alvo = Alvo("192.168.1.10", portas=[80, 443])
    assert alvo.ip == "192.168.1.10"
    assert alvo.portas == [80, 443]
    assert alvo.criado_em.tzinfo is not None
    assert alvo.criado_em.tzinfo == UTC


def test_portscanner():
    alvo = Alvo("192.168.1.10", portas=[80, 22])
    scanner = PortScanner(timeout=30)
    scanner.escanear(alvo)
    assert alvo.status in ["online", "offline"]
    assert isinstance(alvo.portas, list)


def test_vulnscanner():
    alvo = Alvo("192.168.1.10", portas=[80])
    scanner = VulnScanner(timeout=100)
    scanner.escanear(alvo)
    if alvo.status == "vulneravel":
        assert len(alvo.vulnerabilidades) > 0


# pyproject.toml
# Execute "pytest" normalmente após instalar dependências

"""
[project]
name = "aula4-scanner"
version = "0.1.0"
description = "Sistema de escaneamento da aula 4 com testes"
requires-python = ">=3.12"

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project.optional-dependencies]
test = ["pytest"]

"""

# requirements.txt
# Apenas o mínimo necessário para rodar o projeto\pytest
