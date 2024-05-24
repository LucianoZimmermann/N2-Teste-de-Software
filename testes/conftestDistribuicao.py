import pytest
from stat_funcs import StatsN2

vetorDistribuicao1 = [8, 5, 3, 10, 4, 6, 7, 9, 2, 11]
vetorDistribuicao2 = [135, 131, 206, 190, 109, 103,  85,  98, 145, 137]
vetorDistribuicao3 = [70, 50, 825, 987, 217, 22, 36, 46, 57]

@pytest.fixture
def stats():
    return StatsN2()

# Teste verificando valor correto
def test_distribuicao(stats):
    assert stats.skew(vetorDistribuicao1) == 'Distribuição normal'
    assert stats.skew(vetorDistribuicao2) == 'Distribuição positiva'
    assert stats.skew(vetorDistribuicao3) == 'Distribuição positiva'
    print("Teste valores corretos passou")

#Forçando erro e verificando falha
def test_distribuicao_falso(stats):
    assert stats.skew(vetorDistribuicao1) != 'Distribuição negativa'
    assert stats.skew(vetorDistribuicao2) != 'Distribuição negativa'
    assert stats.skew(vetorDistribuicao3) != 'Distribuição normal'
    print("Teste valores errados passou")

if __name__ == "__main__":
    pytest.main()
