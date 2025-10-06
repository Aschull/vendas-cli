### VENDAS-CLI
 - Projeto visa a leitura de um arquivo CSV, filtrar os dados e apresenta-los com a possibilidade de filtar por periodo de data.
 - Pode-se escolher o formato de saida em texto ou JSON.

## OBSERVACAO:
 - Nos requisitos do projeto, pedia um filtro por periodo de data, porem no CSV fornecido nao possuia nenhum campo data, entao eu o inseri na mao.


## INSTALACAO
 - Clonar o projeto: https://github.com/Aschull/vendas-cli#
 - Na pasta do projeto rodar no terminal
 > pipx install . --force

 ## Exemplos de comandos:
  - vendas-cli vendas_exemplo.csv
  - vendas-cli vendas_exemplo.csv --data_inicio 2025-01-05 --data_fim 2025-01-10
  - vendas-cli vendas_exemplo.csv --data_inicio 2025-01-05 --data_fim 2025-01-10 --format json
  - Para formato texto, pode-se informar --format text ou simplesmente nao informar nenhum format, que por padrao sera retornado em text.

## RODAR LOCALMENTE
  - Clonar o projeto: https://github.com/Aschull/vendas-cli#


## Criar ambiente virtual
 - No terminal execute:
  > python3 -m venv venv


## Instalar as bibliotecas
 - No ambiente virtual execute:
  > pip install -r requirementes.txt

## Exemplo de comando ao rodar o codigo local:
  python -m src.cli.main vendas_exemplo.csv --data_inicio 2025-01-05 --data_fim 2025-01-10 --format json


## Rodar Cobertura de codigo
 > pytest --cov=. --cov-report=html

## Desinstalar
 > pipx unistall vendas-cli
