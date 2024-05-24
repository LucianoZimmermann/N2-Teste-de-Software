import pytest
from stat_funcs import StatsN2

vetorVariancia1 = [7, 5, 8, 9, 21, 2, 3, 4, 5]
vetorVariancia2 = [48, 787, 88, 55, 22, 11, 22]
vetorVariancia3 = [70, 50, 825, 987, 217, 22, 36, 46, 57]

@pytest.fixture
def stats():
    return StatsN2()

# Teste verificando valor correto
def test_media_ponderada(stats):
    assert stats.variancia(vetorVariancia1) == 32.36111111111111
    assert stats.variancia(vetorVariancia2) == 80181.61904761905
    assert stats.variancia(vetorVariancia3) == 140440.99999999997
    print("Teste valores corretos passou")

#Forçando erro e verificando falha
def test_media_ponderada_falso(stats):
    assert stats.variancia(vetorVariancia1) != 34
    assert stats.variancia(vetorVariancia2) != 3455
    assert stats.variancia(vetorVariancia3) != 348778
    print("Teste valores errados passou")

if __name__ == "__main__":
    pytest.main()
