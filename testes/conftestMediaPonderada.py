import pytest
from stat_funcs import StatsN2

vetorValores1 = [7, 5, 8, 9, 2]
vetorValores2 = [8, 9, 2, 10, 6]
vetorValores3 = [9, 4, 6, 8, 10]
vetorPesos = [1, 2, 3, 4, 5]

@pytest.fixture
def stats():
    return StatsN2()

# Teste verificando valor correto
def test_media_ponderada(stats):
    assert stats.media_ponderada(vetorValores1, vetorPesos) == 5.8
    assert stats.media_ponderada(vetorValores2, vetorPesos) == 6.8
    assert stats.media_ponderada(vetorValores3, vetorPesos) == 7.8
    print("Teste valores corretos passou")

#Forçando erro e verificando falha
def test_media_ponderada_falso(stats):
    assert stats.media_ponderada(vetorValores1, vetorPesos) != 4
    assert stats.media_ponderada(vetorValores2, vetorPesos) != 8
    assert stats.media_ponderada(vetorValores3, vetorPesos) != 7
    print("Teste valores errados passou")

if __name__ == "__main__":
    pytest.main()
