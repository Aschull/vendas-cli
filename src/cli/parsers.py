import argparse
import logging
from core.csv_processor import CSVProcessor
from reports.sales_report import SalesReport

def main():
    """
	Executa a análise de um arquivo CSV de vendas com filtros de data e formatos de saída.
	"""
    print("CLI funcionando!")
    parser = argparse.ArgumentParser(
		description='Analisa um arquivo CSV de vendas com filtros de data e formatos de saída.')
    parser.add_argument(
		'csv_file',
		type=str,
		help='O caminho para o arquivo CSV de vendas.'
	)
    parser.add_argument(
		'--data_inicio',
		type=str,
		help='Data de início do filtro (formato YYYY-MM-DD).'
	)
    parser.add_argument(
		'--data_fim',
		type=str,
		help='Data de fim do filtro (formato YYYY-MM-DD).'
	)
    parser.add_argument(
		'--format',
		type=str,
		choices=['text', 'json'],
		default='text',
		help='Formato de saída do relatório: "text" (padrão) ou "json".'
	)
    args = parser.parse_args()
    logging.info("Argumentos recebidos: %s", args)

    csv_processor = CSVProcessor(
		file_path=args.csv_file, start_date=args.data_inicio, end_date=args.data_fim)
    results = csv_processor.process_data()

    SalesReport(data=results, report_format=args.format)
