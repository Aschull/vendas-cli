import argparse
import logging
from core.csv_processor import CSVProcessor
from reports.sales_report import SalesReport
from src.interfaces.reader_interface import Reader
from src.interfaces.report_interface import Report


class CliParser:
    """
    Classe para analisar argumentos de linha de comando.
    """
    def __init__(self, csv_processor: Reader, sales_report: Report):
        self.csv_processor: Reader = csv_processor
        self.sales_report: Report = sales_report

    def main(self):
        """
		Executa a análise de um arquivo CSV de vendas com filtros de data e formatos de saída.
		"""
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

        self.csv_processor.set_file_path(args.csv_file)
        self.csv_processor.set_date_filters(args.data_inicio, args.data_fim)
        results = self.csv_processor.process_data()

        # csv_processor = CSVProcessor(
		# 	file_path=args.csv_file, start_date=args.data_inicio, end_date=args.data_fim)
        # results = csv_processor.process_data()

        # SalesReport(data=results, report_format=args.format)
        self.sales_report.generate(data=results, report_format=args.format)
