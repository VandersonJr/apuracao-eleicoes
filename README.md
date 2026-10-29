# Apuração por QR Code do Boletim de Urna (BU)

Protótipo de uma ferramenta **independente** que lê o QR Code do Boletim de Urna impresso,
valida sua autenticidade, soma os votos e indica o candidato mais votado.

> **Aviso:** este projeto NÃO é um sistema oficial e NÃO substitui a totalização do TSE.
> Os resultados são parciais, limitados às seções efetivamente lidas.

## Escopo atual
- Âmbito municipal
- Cargo: prefeito (vereador em fase posterior)

## Status
Fase 0: Fundação e pesquisa. Veja `docs/00-checklist-fase0.md`.

## Como preparar o ambiente
```bash
python -m venv .venv
# Windows:  .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Para o `pyzbar` funcionar em Linux: `sudo apt install libzbar0`. No macOS: `brew install zbar`.

## Estrutura
Veja `docs/03-arquitetura.md`.
