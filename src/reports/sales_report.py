import json
import logging
from typing import Any, Dict, Optional
from interfaces.report_interface import Report


class SalesReport(Report):
    """
    Representa um relatório de vendas que pode ser gerado em diferentes formatos.

    Esta classe processa dados brutos de vendas e os formata em uma saída
    legível (texto) ou em formato de intercâmbio de dados (JSON).
    A geração do relatório é iniciada imediatamente após a inicialização.

    Attributes:
        data (Dict[str, Any]): O dicionário de dados de vendas brutos.
                               O formato esperado do dicionário é:
                               {
                                   'filter_dates': {'start': str, 'end': str},
                                   'best_selling_product': {'product': str, 'quantity': int},
                                   'total_global_revenue': float,
                                   'revenue_per_product': List[Dict[str, Any]]
                               }
        report_format (str): O formato de saída desejado ('text' ou 'json').
    """

    def __init__(self):
        self.data: Optional[Dict[str, Any]] = None
        self.report_format: str = 'text'

    def set_data(self, data: Dict[str, Any]) -> None:
        """Define os dados brutos de vendas que serão usados para gerar o relatório."""
        self.data = data

    def set_report_format(self, report_format: str) -> None:
        """Define o formato de saída desejado ('text' ou 'json')."""
        valid_formats = ['text', 'json']
        if report_format not in valid_formats:
            raise ValueError(
                f"Formato de relatório inválido: '{report_format}'. Escolha entre {valid_formats}")

        self.report_format = report_format

    def generate(self, data: Dict[str, Any], report_format: str) -> Dict[str, Any]:
        """
        Gera o relatório de vendas com base nos dados fornecidos e no formato escolhido.

        Se o formato for 'json', o método format_json_output() é chamado e retorna o relatório em formato JSON.
        Caso contrário, o método format_text_output() é chamado e retorna o relatório em formato de texto.

        Se ocorrer um erro durante a geração do relatório, o erro é registrado no log.
        """
        try:
            self.set_data(data)
            self.set_report_format(report_format)
            if self.report_format == 'json':
                self.format_json_output()
            else:
                self.format_text_output()
            return self.data if self.data is not None else {}
        except Exception as _err:
            logging.error("Error to generate report: %s", _err)
            return {}

    def format_text_output(self):
        """
        Formata o relatório de vendas em formato de texto.

        O relatório consiste em uma linha de título, seguida de uma linha de separação,
        informação sobre o filtro de datas, uma linha de separação, informação sobre o
        produto mais vendido, uma linha de separação, informação sobre o valor total de
        todas as vendas, uma linha de separação e, por fim, uma lista com a receita
        por produto.

        Se o formato for 'text', o método format_text_output() é chamado e retorna o relatório
        em formato de texto.
        """
        if not self.data:
            print("Nenhum dado disponível para gerar o relatório.")
            return

        print("-" * 50)
        print("           RELATÓRIO DE VENDAS           ")
        print(
            f"Filtro de Datas: {self.data.get('filter_dates', {}).get('start', 'N/A')} a {self.data.get('filter_dates', {}).get('end', 'N/A')}")
        print("-" * 50)

        # Produto Mais Vendido
        print("\n## Produto Mais Vendido (por Unidades)")
        best_seller = self.data.get('best_selling_product', {})
        print(
            f"Produto: {best_seller.get('product', 'N/A')} ({best_seller.get('quantity', 'N/A')} unidades)")
        print("-" * 50)

        # Valor Total de Todas as Vendas
        print("\n## Valor Total de Todas as Vendas")
        total_revenue = self.data.get('total_global_revenue')
        if total_revenue is not None:
            print(f"Total Geral: R$ {total_revenue:.2f}")
        else:
            print("Total Geral: N/A")
        print("-" * 50)

        # Total de Vendas por Produto
        print("\n## Total de Vendas (Receita) por Produto")
        for item in self.data.get('revenue_per_product', []):
            product = item.get('product', 'N/A')
            revenue = item.get('revenue', 0.0)
            print(f"- {product.ljust(10)}: R$ {revenue:.2f}")
        print("-" * 50)

    def format_json_output(self):
        """
        Formata o relatório de vendas em formato JSON.

        O relatório em formato JSON é impresso na saída padrão com indentação de 4 espaços e sem caracteres ASCII.

        Se o formato for 'json', o método format_json_output() é chamado e retorna o relatório em formato JSON.
        """
        if not self.data:
            print("Nenhum dado disponível para gerar o relatório.")
            return
        print(json.dumps(self.data, indent=4, ensure_ascii=False))
