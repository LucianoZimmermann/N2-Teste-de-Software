import pytest
from stat_funcs import StatsN2

vetorTeste1 = [7, 5, 8, 9, 21, 2, 3, 4, 5]
vetorTeste2 = [48, 787, 88, 55, 22, 11, 22]
vetorTeste3 = [70, 50, 11, 987, 217, 22, 36, 46, 57]

@pytest.fixture
def stats():
    return StatsN2()

# Teste verificando valor correto
def test_unimodal(stats):
    assert stats.unimodal(vetorTeste1) == 5
    assert stats.unimodal(vetorTeste2) == 22
    assert stats.unimodal(vetorTeste3) == 'Não é unimodal'
    print("Teste valores corretos passou")

#Forçando erro e verificando falha
def test_unimodal_falso(stats):
    assert stats.unimodal(vetorTeste1) != 'Não é unimodal'
    assert stats.unimodal(vetorTeste2) != 'Não é unimodal'
    assert stats.unimodal(vetorTeste3) != 77
    print("Teste valores errados passou")

if __name__ == "__main__":
    pytest.main()
