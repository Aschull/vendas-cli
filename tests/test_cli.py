import pytest
import sys
from src.cli.parsers import main


def test_run_cli_basic(monkeypatch):
    test_args = ["cli.py", "vendas_exemplo.csv"]
    monkeypatch.setattr(sys, "argv", test_args)
    # Não deve levantar exceção
    main()


def test_run_cli_with_format_json(monkeypatch):
    test_args = ["cli.py", "vendas_exemplo.csv", "--format", "json"]
    monkeypatch.setattr(sys, "argv", test_args)
    main()


def test_run_cli_invalid_file(monkeypatch):
    test_args = ["cli.py", "arquivo_inexistente.csv"]
    monkeypatch.setattr(sys, "argv", test_args)
    with pytest.raises(SystemExit):
        main()
