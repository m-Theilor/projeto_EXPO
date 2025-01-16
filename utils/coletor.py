from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def coletar_kabum_com_selenium(categoria_url):
    """
    Função para coletar dados de produtos de uma categoria na Kabum usando Selenium.

    Args:
        categoria_url (str): URL da categoria no site da Kabum.

    Returns:
        list: Lista de dicionários com dados dos produtos.
    """
    # Configurar o navegador (Chrome)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Executa o navegador em modo headless (sem interface gráfica)
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver_path = "C:/Users/amari/Documents/projeto_pessoal_EXPO/chromedriver.exe"

    # Inicializar o navegador
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    print(f"Carregando página: {categoria_url}")
    driver.get(categoria_url)

    # Aguardar o carregamento (adapte o tempo, se necessário)
    driver.implicitly_wait(5)

    # Obter o HTML renderizado
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")
    produtos = []

    # Seleciona os cards de produtos
    items = soup.select("article.sc-27518a44-3.hLEhJe.productCard")
    print(f"Produtos encontrados na página: {len(items)}")

    for item in items:
        try:
            nome = item.select_one("span.sc-d79c9c3f-0.nlmfp.sc-27518a44-9.iJKRqI.nameCard").text.strip()
            preco = item.select_one("span.sc-57f0fd6e-2.hjJfoh.priceCard").text.strip().replace("R$", "").replace(".", "").replace(",", ".").strip()
            link = "https://www.kabum.com.br" + item.select_one("a.sc-27518a44-4.kVoakD.productLink")["href"]

            produtos.append({
                "categoria": "Hardware",  # Ajuste conforme a categoria
                "marca": "Desconhecida",  # Adicionar lógica para capturar a marca, se disponível
                "modelo": nome,
                "especificacoes": "",  # Especificações detalhadas podem ser adicionadas futuramente
                "valor": float(preco) if preco else 0,
                "nome_loja": "Kabum",
                "link": link,
            })
        except Exception as e:
            print(f"Erro ao processar item: {e}")
    return produtos
