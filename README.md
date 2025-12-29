# Crawler Estadão (ETL Pipeline)

Este projeto realiza a extração, transformação e carregamento (ETL) de notícias do portal Estadão, convertendo dados não estruturados da web em arquivos `.csv` organizados.

---

## Instalação e Configuração

Siga os passos abaixo no seu terminal para configurar o ambiente:

**1. Clonar o repositório:**
```bash
git clone [https://github.com/seu-usuario/crawler-estadao.git](https://github.com/seu-usuario/crawler-estadao.git)
cd crawler-estadao
```

**2. Instalar dependências:**
```bash
pip install -r requirements.txt
```

---

## Execução e Demonstração

Ao executar o script principal, você verá o progresso da extração em tempo real:

```text
$ python app.py

```

## Detalhes do ETL

### 1. Extração (Extract)
Utiliza a biblioteca `Requests` para baixar o HTML e o `BeautifulSoup` para navegar na árvore DOM, isolando o container principal da notícia.

### 2. Transformação (Transform)
* **Regex:** Limpeza de tags residuais e extração de metadados ocultos no JS.
* **Unidecode:** Normalização de strings para evitar erros de encoding no CSV.
* **Pandas:** Estruturação dos dados e remoção de duplicatas.

### 3. Carregamento (Load)
Verificação de arquivos existentes via biblioteca `os` e salvamento incremental em CSV.
