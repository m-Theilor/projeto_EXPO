import pytest
from utils.coletor import coletar_kabum_com_selenium

# URL de exemplo
url_categoria = "https://www.kabum.com.br/hardware"

def test_coletar_kabum_funciona():
    """
    Testa se a função coletar_kabum_com_selenium coleta dados corretamente.
    """
    produtos = coletar_kabum_com_selenium(url_categoria)

    # Verificar se a função retornou produtos
    assert isinstance(produtos, list), "O resultado deve ser uma lista"
    assert len(produtos) > 0, "A lista de produtos não pode estar vazia"

    # Verificar os campos de cada produto
    for produto in produtos:
        assert "modelo" in produto, "Cada produto deve ter um campo 'modelo'"
        assert "valor" in produto, "Cada produto deve ter um campo 'valor'"
        assert "link" in produto, "Cada produto deve ter um campo 'link'"
        assert produto["modelo"], "O campo 'modelo' não pode estar vazio"
        assert produto["valor"] >= 0, "O preço do produto deve ser maior ou igual a zero"
        assert produto["link"].startswith("https://www.kabum.com.br"), "O link deve ser válido"

def test_url_invalida():
    """
    Testa como a função lida com uma URL inválida.
    """
    produtos = coletar_kabum_com_selenium("https://www.kabum.com.br/nao-existe")
    assert produtos == [], "A função deve retornar uma lista vazia para URLs inválidas"

def test_excecoes():
    """
    Testa se a função trata exceções corretamente.
    """
    with pytest.raises(Exception):
        coletar_kabum_com_selenium(None)  # URL inválida
