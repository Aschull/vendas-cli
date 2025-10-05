import json
import logging
from typing import Any, Dict
from interfaces.report_interface import Report

class SalesReport(Report):
    def __init__(self, data: Dict[str, Any], report_format: str = 'text'):
        self.data: Dict[str, Any] = data
        self.report_format: str = report_format
        self.generate()

    def generate(self):
        try:
            if self.report_format == 'json':
                self.format_json_output()
                return
            self.format_text_output()
            return
        except Exception as _err:
            logging.error("Error to generate report: %s", _err)

    def format_text_output(self):
        print("-" * 50)
        print("           RELATÓRIO DE VENDAS           ")
        print(f"Filtro de Datas: {self.data['filter_dates']['start'] or 'N/A'} a {self.data['filter_dates']['end'] or 'N/A'}")
        print("-" * 50)

        # Produto Mais Vendido
        print("\n## Produto Mais Vendido (por Unidades)")
        best_seller = self.data['best_selling_product']
        print(f"Produto: {best_seller['product']} ({best_seller['quantity']} unidades)")
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
        print(json.dumps(self.data, indent=4, ensure_ascii=False))
