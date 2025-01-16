import requests
from bs4 import BeautifulSoup
from utils.coletor import coletar_kabum_com_selenium

# URL de exemplo para a categoria de placas de vídeo na Kabum
url_categoria = "https://www.kabum.com.br/hardware/placas-mae"

# Coletar dados
print(f"Realizando a coleta da URL: {url_categoria}")
produtos = coletar_kabum_com_selenium(url_categoria)

# Verifique se a lista de produtos está vazia
if not produtos:
    print("Nenhum produto foi coletado. Verifique os seletores e a página alvo.")
else:
    # Exibir os dados coletados
    for produto in produtos:
        print(produto)
