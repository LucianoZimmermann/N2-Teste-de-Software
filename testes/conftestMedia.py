import pytest
from stat_funcs import StatsN2

vetorTeste1 = [10, 11, 12, 43, 54]
vetorTeste2 = [21, 101, 15, 44, 54]
vetorTeste3 = [25, 70, 70, 100, 15]

@pytest.fixture
def stats():
    return StatsN2()

# Teste verificando valor correto
def test_media(stats):
    assert stats.media(vetorTeste1) == 26
    assert stats.media(vetorTeste2) == 47
    assert stats.media(vetorTeste3) == 56
    print("Teste valores corretos passou")

#Forçando erro e verificando falha
def test_media_Falso(stats):
    assert stats.media(vetorTeste1) != 20
    assert stats.media(vetorTeste2) != 75
    assert stats.media(vetorTeste3) != 52
    print("Teste valores errados passou")

if __name__ == "__main__":
    pytest.main()
