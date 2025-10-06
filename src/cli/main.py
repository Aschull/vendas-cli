import logging
from core.csv_processor import CSVProcessor
from reports.sales_report import SalesReport
from cli.parsers import CliParser

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    """
    Função principal que inicializa o sistema, injeta dependências e executa o CLI Parser.
    Esta função é o ponto de entrada (entry point) da aplicação.
    """
    try:
        csv_processor = CSVProcessor()
    except TypeError:
        csv_processor = CSVProcessor()

    sales_report = SalesReport()

    cli_parser = CliParser(
        csv_processor=csv_processor,
        sales_report=sales_report
    )

    cli_parser.main()

if __name__ == '__main__':
    main()
