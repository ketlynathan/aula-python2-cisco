import pytest
from src.models.alvo import Alvo, InvalidIPError
from datetime import timezone


def test_alvo_criacao_valida():
    alvo = Alvo("192.168.1.10", portas=[80, 443])
    assert alvo.ip == "192.168.1.10"
    assert alvo.portas == [80, 443]
    assert alvo.criado_em.tzinfo is not None
    assert alvo.criado_em.tzinfo == timezone.utc


def test_alvo_ip_invalido():
    with pytest.raises(InvalidIPError):
        Alvo("999.999.999.999")
