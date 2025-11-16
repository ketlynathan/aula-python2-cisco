from src.models.alvo import Alvo
from src.scanners.port_scanner import PortScanner
from src.scanners.vuln_scanner import VulnScanner


def test_port_scanner_adiciona_vuln():


alvo = Alvo("192.168.1.10", portas=[80])
ps = PortScanner(alvo, portas_a_testar=[22, 80])
ps.executar_scan()
assert alvo.status == "online"
assert 22 in alvo.portas
assert "ssh_config_inseguro" in alvo.get_vulns()


def test_vuln_scanner_adiciona_vulns():
    alvo = Alvo("192.168.1.11", portas=[80])
    vs = VulnScanner(alvo, scripts=["smb_vuln", "http_vuln"])
    vs.executar_scan()
    assert alvo.status == "vulneravel"
    assert "smb_vuln_detectado" in alvo.get_vulns()
    assert "http_vuln_detectado" in alvo.get_vulns()
