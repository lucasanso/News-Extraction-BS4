import requests
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime
import pytz # Python timezone
import pandas as pd # Armazenar os dados 
import re # Regular Expressions para a validação de cada uma das notícias
from keywords import KEYWORDS
from keywords import VALIDATION_KEYWORDS
from unidecode import unidecode # Para formatar cada texto de cada notícia para tornar mais preciso o uso de RE

# Passaríamos argumentos aqui na classe se estivéssemos utilizando herança.
class EstadaoSpider:

    def __init__(self, keyword, list):
        self.keyword = keyword
        self.noticias_aceitas = []
        self.noticias_recusadas = []
        self.lista_urls = list
        self.start_requests(self.lista_urls)

    # Método que faz a requisição para obter o HTML da página
    def start_requests(self, list):
        for url in list:
            response = requests.get(url)

            if response.status_code == 200:
                print(f"Extraindo notícia da url: {url}")

                self._parser(response.text, url)
                
            else:
                print(f"Não foi possível acessar a url: {url}.")

        self.load_accepted(self.noticias_aceitas)
        self.load_unaccepted(self.noticias_recusadas)
        self.print_news(self.noticias_aceitas)
        self.print_news(self.noticias_recusadas)

    # Método que só deve extrair o conteúdo desejado do HTML da notícia.
    # Método protected: não deve ser usado fora da classe
    def _parser (self, html, url):
        html_bs4 = BeautifulSoup(html, "html.parser")

        item = {}

        acquisition_date = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime(r'%d-%m-%Y')
        last_update = acquisition_date
        raw_publication_date = html_bs4.select_one("time").text
        date = raw_publication_date.strip()[:10] # Strip remove espaços ou quebras de linha invisíveis e slicing para pegar somente uma parte da data.
        title = html_bs4.select_one("h1").text

        raw_article = html_bs4.select_one("#content")

        paragrafos = ""
        paragrafo = raw_article.select_one("p")

        # Concantenação dos parágrafos das notícias
        while paragrafo:
            paragrafos = paragrafos + paragrafo.text
            paragrafo = paragrafo.find_next("p")

        print("A URL foi totalmente extraída.")

        if self.validation_article(paragrafos):
            item["acquisition_date"] = acquisition_date
            item["publication_date"] = date
            item["accepted_by"] = self.validation_article(paragrafos)
            item["article"] = paragrafos
            item["keyword"] = self.keyword
            item["last_update"] = last_update
            item["title"] = title
            item["url"] = url
            item["tags"] = None
            item["manual_relevance_class"] = None

            self.noticias_aceitas.append(item)
        else:
            item["url"] = url
            item["accepted_by"] = self.validation_article(paragrafos)
            self.noticias_recusadas.append(item)

        return f"Notícia cuja URL é {url} foi verificada."
    
    # Método para salvar notícia depois de limpa
    # Do jeito que está aqui, sempre que eu rodar o código, vai sobrescrever o que já tinha...
    # Ver a biblioteca pandas para conseguir adicionar uma linha de .csv
    def load_accepted(self, noticias):
        data_frame = pd.DataFrame(noticias)
        data_frame.to_csv("news_accepted.csv")
        
        print(f"Notícias aceitas foram armazenadas.")


    # Método para salvar notícia depois de limpa
    # Do jeito que está aqui, sempre que eu rodar o código, vai sobrescrever o que já tinha...
    # Ver a biblioteca pandas para conseguir adicionar uma linha de .csv
    def load_unaccepted(self, noticias):
        data_frame = pd.DataFrame(noticias)
        data_frame.to_csv("unaccepted_news.csv")

        print(f"Notícia não aceita foi armazenada.")

    # Método que exibe cada uma das notícias de qualquer lista de notícias
    def print_news(self, list_news):
        for i in range (0, len(list_news)):
            pprint(list_news[i], sort_dicts=False)

    # Método que valida as palavras-chave: OK
    def validation_article(self, article):
        if not article: return False
        # Lógica de validação de primeira e segunda tabelas
        GANGS_NAMES = VALIDATION_KEYWORDS["GANGS"] + VALIDATION_KEYWORDS["ORGANIZED CRIME"]
        gang = False 
        for p in GANGS_NAMES:
            if re.findall(p, unidecode(article.lower()), re.I):
                gang = p; break
        
        activity = False
        GANGS_ACTIONS = VALIDATION_KEYWORDS["DRUGS"] + VALIDATION_KEYWORDS["ARMED INTERACTIONS"]
        for p in GANGS_ACTIONS:
            if re.findall(p, unidecode(article.lower()), re.I):
                activity = p; break
            
        return f"{gang} - {activity}" if (gang and activity) else False
    
    # Método que retorna todas as URLs para pular caso já tenha sido percorrida (em conjunto com lógica de evitar duplicação)
    def get_all_urls(self): 
        pass

