import pytest
from stat_funcs import StatsN2

vetorTeste1 = [7, 5, 8, 9, 21, 2, 3, 4, 5]
vetorTeste2 = [48, 787, 88, 55, 22, 11, 22]
vetorTeste3 = [70, 50, 11, 987, 217, 22, 36, 46, 57]

@pytest.fixture
def stats():
    return StatsN2()

# Teste verificando valor correto
def test_amodal(stats):
    assert stats.amodal(vetorTeste1) == 'Existe moda'
    assert stats.amodal(vetorTeste2) == 'Existe moda'
    assert stats.amodal(vetorTeste3) == 'Não existe moda'
    print("Teste valores corretos passou")

#Forçando erro e verificando falha
def test_amodal_falso(stats):
    assert stats.amodal(vetorTeste1) != 'Não existe moda'
    assert stats.amodal(vetorTeste2) != 'Não existe moda'
    assert stats.amodal(vetorTeste3) != 'Existe moda'
    print("Teste valores errados passou")

if __name__ == "__main__":
    pytest.main()
