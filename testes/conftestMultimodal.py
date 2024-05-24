import pytest
from stat_funcs import StatsN2

vetorTeste1 = [7, 5, 8, 9, 21, 2, 3, 4, 5]
vetorTeste2 = [48, 787, 88, 55, 22, 11, 22]
vetorTeste3 = [70, 50, 11, 987, 217, 22, 36, 46, 57]

@pytest.fixture
def stats():
    return StatsN2()

# Teste verificando valor correto
def test_multimodal(stats):
    assert stats.multimodal(vetorTeste1) == 'Não é multimodal'
    assert stats.multimodal(vetorTeste2) == 'Não é multimodal'
    assert stats.multimodal(vetorTeste3) == [70, 50, 11, 987, 217, 22, 36, 46, 57]
    print("Teste valores corretos passou")

#Forçando erro e verificando falha
def test_multimodal_falso(stats):
    assert stats.multimodal(vetorTeste1) != vetorTeste1
    assert stats.multimodal(vetorTeste2) != vetorTeste2
    assert stats.multimodal(vetorTeste3) != 'Não é multimodal'
    print("Teste valores errados passou")

if __name__ == "__main__":
    pytest.main()
