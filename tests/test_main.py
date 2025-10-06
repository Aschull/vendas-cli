import pytest
import sys
from unittest.mock import Mock, patch, MagicMock
from cli.main import main


class TestMain:
    """Testes unitários para o módulo main.py"""

    @patch('cli.main.CliParser')
    @patch('cli.main.SalesReport')
    @patch('cli.main.CSVProcessor')
    def test_main_inicializa_dependencias_corretamente(
        self, mock_csv_processor, mock_sales_report, mock_cli_parser
    ):
        """Testa se main() inicializa todas as dependências corretamente"""
        # Arrange
        mock_csv_instance = Mock()
        mock_sales_instance = Mock()
        mock_cli_instance = Mock()

        mock_csv_processor.return_value = mock_csv_instance
        mock_sales_report.return_value = mock_sales_instance
        mock_cli_parser.return_value = mock_cli_instance

        # Act
        main()

        # Assert
        mock_csv_processor.assert_called_once()
        mock_sales_report.assert_called_once()
        mock_cli_parser.assert_called_once_with(
            csv_processor=mock_csv_instance,
            sales_report=mock_sales_instance
        )
        mock_cli_instance.main.assert_called_once()

    @patch('cli.main.CliParser')
    @patch('cli.main.SalesReport')
    @patch('cli.main.CSVProcessor')
    def test_main_executa_cli_parser(
        self, mock_csv_processor, mock_sales_report, mock_cli_parser
    ):
        """Testa se main() executa o método main() do CliParser"""
        # Arrange
        mock_cli_instance = Mock()
        mock_cli_parser.return_value = mock_cli_instance

        # Act
        main()

        # Assert
        mock_cli_instance.main.assert_called_once()

    @patch('cli.main.CliParser')
    @patch('cli.main.SalesReport')
    @patch('cli.main.CSVProcessor')
    def test_main_trata_typeerror_em_csv_processor(
        self, mock_csv_processor, mock_sales_report, mock_cli_parser
    ):
        """Testa se main() trata TypeError ao criar CSVProcessor"""
        # Arrange
        mock_csv_instance = Mock()
        # Simula TypeError na primeira chamada, sucesso na segunda
        mock_csv_processor.side_effect = [TypeError(), mock_csv_instance]
        mock_cli_instance = Mock()
        mock_cli_parser.return_value = mock_cli_instance

        # Act
        main()

        # Assert
        assert mock_csv_processor.call_count == 2
        mock_cli_instance.main.assert_called_once()

    @patch('cli.main.CliParser')
    @patch('cli.main.SalesReport')
    @patch('cli.main.CSVProcessor')
    def test_main_injeta_dependencias_no_cli_parser(
        self, mock_csv_processor, mock_sales_report, mock_cli_parser
    ):
        """Testa se main() injeta corretamente as dependências no CliParser"""
        # Arrange
        mock_csv_instance = Mock()
        mock_sales_instance = Mock()

        mock_csv_processor.return_value = mock_csv_instance
        mock_sales_report.return_value = mock_sales_instance

        # Act
        main()

        # Assert
        mock_cli_parser.assert_called_once()
        call_args = mock_cli_parser.call_args
        assert call_args[1]['csv_processor'] == mock_csv_instance
        assert call_args[1]['sales_report'] == mock_sales_instance

    @patch('cli.main.CliParser')
    @patch('cli.main.SalesReport')
    @patch('cli.main.CSVProcessor')
    def test_main_cria_instancias_na_ordem_correta(
        self, mock_csv_processor, mock_sales_report, mock_cli_parser
    ):
        """Testa se main() cria as instâncias na ordem correta"""
        # Arrange
        call_order = []

        mock_csv_processor.side_effect = lambda *args, **kwargs: call_order.append('csv') or Mock()
        mock_sales_report.side_effect = lambda *args, **kwargs: call_order.append('sales') or Mock()
        mock_cli_parser.side_effect = lambda *args, **kwargs: call_order.append('cli') or Mock()

        # Act
        main()

        # Assert
        assert call_order == ['csv', 'sales', 'cli']

    @patch('cli.main.CliParser')
    @patch('cli.main.SalesReport')
    @patch('cli.main.CSVProcessor')
    def test_main_com_excecao_no_cli_parser(
        self, mock_csv_processor, mock_sales_report, mock_cli_parser
    ):
        """Testa se exceções no CliParser.main() são propagadas"""
        # Arrange
        mock_cli_instance = Mock()
        mock_cli_instance.main.side_effect = Exception("Erro no CLI")
        mock_cli_parser.return_value = mock_cli_instance

        # Act & Assert
        with pytest.raises(Exception, match="Erro no CLI"):
            main()

    @patch('cli.main.CliParser')
    @patch('cli.main.SalesReport')
    @patch('cli.main.CSVProcessor')
    def test_main_com_excecao_no_sales_report(
        self, mock_csv_processor, mock_sales_report, mock_cli_parser
    ):
        """Testa se exceções no SalesReport são propagadas"""
        # Arrange
        mock_sales_report.side_effect = Exception("Erro no SalesReport")

        # Act & Assert
        with pytest.raises(Exception, match="Erro no SalesReport"):
            main()
