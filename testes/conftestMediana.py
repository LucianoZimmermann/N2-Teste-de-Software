import pytest
from stat_funcs import StatsN2

vetorTest1 = [11, 188, 447, 202, 488, 478, 55]
vetorTest2 = [11, 188, 44, 254, 222, 499, 505]
vetorTest3 = [87, 45, 65, 56, 87, 32, 888, 962 ]

@pytest.fixture
def stats():
    return StatsN2()

# Teste verificando valor correto
def test_mediana(stats):
    assert stats.mediana(vetorTest1) == 202
    assert stats.mediana(vetorTest2) == 222
    assert stats.mediana(vetorTest3) == 76
    print("Teste valores corretos passou")

#Forçando erro e verificando falha
def test_mediana_falso(stats):
    assert stats.mediana(vetorTest1) != 20
    assert stats.mediana(vetorTest2) != 75
    assert stats.mediana(vetorTest3) != 22
    print("Teste valores errados passou")

if __name__ == "__main__":
    pytest.main()
