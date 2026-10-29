"""Fase 4: soma de votos e ranking (majoritário)."""


def apurar(votos_por_candidato: dict[int, int]) -> dict:
    total = sum(votos_por_candidato.values())
    ranking = sorted(votos_por_candidato.items(), key=lambda x: x[1], reverse=True)
    if not ranking:
        return {"lider": None, "empate": False, "percentual": 0, "ranking": []}
    lider, votos_lider = ranking[0]
    empate = len(ranking) > 1 and ranking[1][1] == votos_lider
    return {
        "lider": None if empate else lider,
        "empate": empate,
        "percentual": round(100 * votos_lider / total, 2) if total else 0,
        "ranking": ranking,
    }
