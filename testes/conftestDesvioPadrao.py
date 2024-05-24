import pytest
from stat_funcs import StatsN2

variancia1 = 54
variancia2 = 5
variancia3 = 454

@pytest.fixture
def stats():
    return StatsN2()

# Teste verificando valor correto
def test_dPadrao(stats):
    assert stats.dpadrao(variancia1) == 7.3484692283495345
    assert stats.dpadrao(variancia2) == 2.23606797749979
    assert stats.dpadrao(variancia3) == 21.307275752662516
    print("Teste valores corretos passou")

#Forçando erro e verificando falha
def test_dPadrao_falso(stats):
    assert stats.dpadrao(variancia1) != 7
    assert stats.dpadrao(variancia2) != 2
    assert stats.dpadrao(variancia3) != 21
    print("Teste valores errados passou")

if __name__ == "__main__":
    pytest.main()
