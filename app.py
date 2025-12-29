from parser_estadao import EstadaoSpider

# -------------------------------------------------------------------------------- #
# BLOCO DE TESTE DO SPIDER

# Aqui podemos passar quantas URLs quisermos
lista_urls = ["https://www.estadao.com.br/internacional/por-dentro-da-disputa-pela-politica-externa-do-maga/",
            "https://www.estadao.com.br/politica/prefeito-de-diadema-e-condenado-por-ligar-assessor-de-lula-a-marcola-e-crime-organizado-npr/",
            "https://www.estadao.com.br/politica/lula-diz-que-dinheiro-e-influencia-nao-pararao-a-pf-e-que-combate-a-faccoes-chegou-ao-andar-de-cima/",
            "https://www.estadao.com.br/saude/adultos-podem-tomar-a-vacina-contra-hpv-especialistas-tiram-duvidas-sobre-o-imunizante-nprm/",
            "https://www.estadao.com.br/link/empresas/ricacos-do-vale-do-silicio-miram-algoritmos-e-ciencia-de-dados-para-gerarem-os-bebes-perfeitos/",
            "https://www.estadao.com.br/brasil/serial-killer-da-rotatoria-foge-de-prisao-de-seguranca-maxima-governo-ve-elo-de-detento-com-o-pcc-npr/",
            "https://www.estadao.com.br/economia/negocios/de-postos-de-gasolina-a-fintechs-como-o-crime-se-infiltrou-no-dia-a-dia-dos-negocios-no-brasil/",
            "https://www.estadao.com.br/politica/prefeito-de-diadema-e-condenado-por-ligar-assessor-de-lula-a-marcola-e-crime-organizado-npr/",
            "https://www.estadao.com.br/sao-paulo/operacao-da-pm-na-favela-do-moinho-deixa-suspeito-morto-apos-troca-de-tiros-npr/"]

# Dicionário de configurações do scraper 
CONFIGS_BOT = {'KEYWORD':'pcc'}

def executar():
    print("Iniciando bot do portal Estadão...")
    bot_init = EstadaoSpider(keyword=CONFIGS_BOT["KEYWORD"], list=lista_urls)

if __name__ == "__main__":
    executar()