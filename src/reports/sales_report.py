import json
import logging
from typing import Any, Dict
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
    def __init__(self, data: Dict[str, Any], report_format: str = 'text'):
        self.data: Dict[str, Any] = data
        self.report_format: str = report_format
        self.generate()

    def generate(self):
        """
        Gera o relatório de vendas com base nos dados fornecidos e no formato escolhido.

        Se o formato for 'json', o método format_json_output() é chamado e retorna o relatório em formato JSON.
        Caso contrário, o método format_text_output() é chamado e retorna o relatório em formato de texto.

        Se ocorrer um erro durante a geração do relatório, o erro é registrado no log.
        """
        try:
            if self.report_format == 'json':
                self.format_json_output()
                return
            self.format_text_output()
            return
        except Exception as _err:
            logging.error("Error to generate report: %s", _err)

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
        print("-" * 50)
        print("           RELATÓRIO DE VENDAS           ")
        print(
            f"Filtro de Datas: {self.data['filter_dates']['start'] or 'N/A'} a {self.data['filter_dates']['end'] or 'N/A'}")
        print("-" * 50)

        # Produto Mais Vendido
        print("\n## Produto Mais Vendido (por Unidades)")
        best_seller = self.data['best_selling_product']
        print(
            f"Produto: {best_seller['product']} ({best_seller['quantity']} unidades)")
        print("-" * 50)

        # Valor Total de Todas as Vendas
        print("\n## Valor Total de Todas as Vendas")
        print(f"Total Geral: R$ {self.data['total_global_revenue']:.2f}")
        print("-" * 50)

        # Total de Vendas por Produto
        print("\n## Total de Vendas (Receita) por Produto")
        for item in self.data['revenue_per_product']:
            product = item['product']
            revenue = item['revenue']
            print(f"- {product.ljust(10)}: R$ {revenue:.2f}")
        print("-" * 50)

    def format_json_output(self):
        """
        Formata o relatório de vendas em formato JSON.

        O relatório em formato JSON é impresso na saída padrão com indentação de 4 espaços e sem caracteres ASCII.

        Se o formato for 'json', o método format_json_output() é chamado e retorna o relatório em formato JSON.
        """
        print(json.dumps(self.data, indent=4, ensure_ascii=False))
