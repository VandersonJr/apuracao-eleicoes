"""Fase 2: transforma o texto do QR em um objeto BoletimUrna."""
from dataclasses import dataclass, field


@dataclass
class BoletimUrna:
    municipio: str = ""
    zona: int = 0
    secao: int = 0
    cargo: str = ""
    turno: int = 1
    brancos: int = 0
    nulos: int = 0
    votos: dict[int, int] = field(default_factory=dict)  # numero do candidato -> votos


def interpretar(texto_qr: str) -> BoletimUrna:
    raise NotImplementedError("Implementar na Fase 2, seguindo docs/04-formato-qr.md")
