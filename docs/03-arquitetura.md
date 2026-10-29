# Arquitetura

```
Foto do QR -> leitor_qr -> parser_bu -> validador -> banco -> apuracao -> app (Streamlit)
```

| Módulo | Responsabilidade |
|---|---|
| `src/leitor_qr.py` | imagem -> texto do QR |
| `src/parser_bu.py` | texto -> objeto `BoletimUrna` |
| `src/validador.py` | assinatura e duplicidade |
| `src/banco.py` | persistência em SQLite |
| `src/apuracao.py` | soma, percentual, ranking |
| `src/app.py` | interface Streamlit |

Decisões: ver ADRs em `docs/adr/` (a criar).
