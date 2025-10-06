import pytest
import sys
from src.cli.parsers import CliParser
from src.core.csv_processor import CSVProcessor
from src.reports.sales_report import SalesReport


def test_run_cli_basic(monkeypatch):
    test_args = ["cli.py", "vendas_exemplo.csv"]
    monkeypatch.setattr(sys, "argv", test_args)
    # Não deve levantar exceção
    csv_processor = CSVProcessor()
    sales_report = SalesReport()

    cli_parser = CliParser(
        csv_processor=csv_processor,
        sales_report=sales_report
    )

    cli_parser.main()


def test_run_cli_with_format_json(monkeypatch):
    test_args = ["cli.py", "vendas_exemplo.csv", "--format", "json"]
    monkeypatch.setattr(sys, "argv", test_args)
    csv_processor = CSVProcessor()
    sales_report = SalesReport()

    cli_parser = CliParser(
        csv_processor=csv_processor,
        sales_report=sales_report
    )

    cli_parser.main()


def test_run_cli_invalid_file(monkeypatch):
    test_args = ["cli.py", "arquivo_inexistente.csv"]
    monkeypatch.setattr(sys, "argv", test_args)
    with pytest.raises(SystemExit):
        csv_processor = CSVProcessor()
        sales_report = SalesReport()

        cli_parser = CliParser(
            csv_processor=csv_processor,
            sales_report=sales_report
        )

        cli_parser.main()
