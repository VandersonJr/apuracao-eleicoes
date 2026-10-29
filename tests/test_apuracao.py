from src.apuracao import apurar


def test_lider_simples():
    r = apurar({13: 600, 45: 400})
    assert r["lider"] == 13
    assert r["percentual"] == 60.0
    assert not r["empate"]


def test_empate():
    r = apurar({13: 500, 45: 500})
    assert r["lider"] is None
    assert r["empate"]


def test_sem_votos():
    assert apurar({})["lider"] is None
