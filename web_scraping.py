# Importando pacotes

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import duckdb

# Configuração do Selenium
options = Options()
options.add_argument("--headless")  # Executa em segundo plano
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome()

# Lista de categorias para buscar (URLs das categorias do Mercado Livre)
categorias = [
    "https://lista.mercadolivre.com.br/figure-action#D[A:figure%20action,L:undefined]",
    "https://lista.mercadolivre.com.br/decora%C3%A7%C3%A3o-escritorio#D[A:Decora%C3%A7%C3%A3o%20escritorio]",
    "https://lista.mercadolivre.com.br/decora%C3%A7%C3%A3o-casa#D[A:decora%C3%A7%C3%A3o%20casa]",
    "https://lista.mercadolivre.com.br/organizadores#D[A:Organizadores]",
    "https://lista.mercadolivre.com.br/suporte-headfone#D[A:suporte%20headfone]",
    "https://lista.mercadolivre.com.br/suporte-controle#D[A:suporte%20controle]",
    "https://lista.mercadolivre.com.br/estatueta#D[A:Estatueta]",
    "https://lista.mercadolivre.com.br/luminaria#D[A:luminaria]"
]


lista_nome = []
lista_avaliacoes = []
lista_nota = []
lista_preco = []
lista_link = []
lista_categoria =[]

# Looping para os links selecionados nas categorias
for categoria in categorias:
    driver.get(categoria)
    time.sleep(2)
    
    categoria_nome = driver.find_element(By.TAG_NAME, "h1").text
    qtd_produtos = 10000

# Looping para as páginas
    for páginas in range(50):

        produtos = driver.find_elements(By.CLASS_NAME,"ui-search-layout__item")
        time.sleep(1)
        for produto in produtos:
            
            try:
                nome = produto.find_element(By.CLASS_NAME, "poly-component__title").text
            except:
                nome = "nd"
            try:
                qtd_avaliacoes = produto.find_element(By.CLASS_NAME, "poly-reviews__total").text
            except:
                qtd_avaliacoes = "nd"
            try:
                nota = produto.find_element(By.CLASS_NAME, "poly-reviews__rating").text
            except:
                nota = "nd"
            try:
                preco = produto.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
            except:
                preco = "nd"
            try:
                link = produto.find_element(By.TAG_NAME, "a").get_attribute("href")
            except:
                link = "nd"

            lista_categoria.append(categoria_nome)
            lista_nome.append(nome)
            lista_avaliacoes.append(qtd_avaliacoes)
            lista_nota.append(nota)
            lista_preco.append(preco)
            lista_link.append(link)

            if len(lista_nome) >= qtd_produtos:
                break

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
        try:
            driver.find_element(By.XPATH,'//*[@id="root-app"]/div/div[3]/section/nav/ul/li[12]/a').click()
        except:
                print("página acabou")
                break
        time.sleep(2)

df = pd.DataFrame({
    'Nome': lista_nome,
    'qtd_Avaliações': lista_avaliacoes,
    'Preco': lista_preco,
    'Categoria': lista_categoria,
    'Link': lista_link,
    'Nota': lista_nota})

df = df[df['Nome'] != "nd"]

con = duckdb.connect("mercadolivre.db")  
con.register('produtos', df)

con.close()

df.to_csv('mercadolivre.csv')

print('Executado com sucesso')
