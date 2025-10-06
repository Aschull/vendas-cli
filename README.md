### VENDAS-CLI
 - Projeto visa a leitura de um arquivo CSV, filtrar os dados e apresenta-los com a possibilidade de filtar por periodo de data.
 - Pode-se escolher o formato de saida em texto ou JSON.


## ADICIONAR SRC NO PATH
 - Na raiz do projeto execute:
  > export PYTHONPATH=$PYTHONPATH:$(pwd)/src


## Criar ambiente virtual
 - No terminal execute:
  > python3 -m venv venv


## Instalar as bibliotecas
 - No ambiente virtual execute:
  > pip install -r requirementes.txt


## Rodar Cobertura de codigo
 > pytest --cov=. --cov-report=html


## INSTALACAO
 - Clonar o projeto: https://github.com/Aschull/vendas-cli#
 - Na pasta do projeto rodar no terminal
 > pipx install .


## Exemplos de comandos:
  - vendas-cli vendas_exemplo.csv
  - vendas-cli vendas_exemplo.csv --data_inicio 2025-01-05 --data_fim 2025-01-10
  - vendas-cli vendas_exemplo.csv --data_inicio 2025-01-05 --data_fim 2025-01-10 --format json


## Exemplo de comando ao rodar o codigo local:
  python -m src.cli.main vendas_exemplo.csv --data_inicio 2025-01-05 --data_fim 2025-01-10 --format json


## Desinstalar
 > pipx unistall vendas-cli


### OBSERVACAO:
 - Nos requisitos do projeto, pedia um filtro por periodo de data, porem no CSV fornecido nao possuia nenhum campo data, entao eu o inseri na mao.