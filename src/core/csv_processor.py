import csv
from datetime import datetime
import logging
import sys
from typing import Any, Dict, List, Optional
from interfaces.reader_interface import Reader
from utils.helpers import (
    calculate_sales,
    convert_sale_values,
    datetime_treat,
    parse_date,
    update_aggregates,
    parser_to_dict_list
)


class CSVProcessor(Reader):
    """
    Processador de dados de vendas baseado em CSV.
    """

    def __init__(
        self,
        file_path: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ):
        self._data_path: str = file_path
        self.start_date: Optional[str] = start_date
        self.end_date: Optional[str] = end_date
        self._headers: List[str] = []
        self.date_format = "%Y-%m-%d"
        self.global_revenue: float = 0.0
        self.total_global_revenue: float = 0.0
        self.revenue_per_product: Dict[str, float] = {}
        self.quantity_per_product: Dict[str, int] = {}

    def process_data(self) -> Dict[str, Any]:
        """
        Processa o arquivo CSV e retorna um dicionário com os resultados agregados.
        
        Chama o método process_csv_rows() para processar as linhas do arquivo CSV e,
        em seguida, chama o método aggregate_results() para calcular os resultados
        agregados e retorná-los como um dicionário.
        
        Returns:
            Dict[str, Any]: Um dicionário com os resultados agregados.
        """
        self.process_csv_rows()
        return self.aggregate_results()

    def process_csv_rows(self):
        """
        Processa as linhas do arquivo CSV e atualiza os atributos de receita e quantidade.

        Lê o arquivo CSV e itera sobre as linhas do arquivo. Para cada linha, verifica se a
        data de venda está dentro do filtro de data e, se sim, atualiza os atributos de
        receita e quantidade.

        Se houver um erro de formatação na linha ou se a data de venda estiver fora do
        filtro de data, a linha é ignorada e o processo continua.

        Se houver um erro de leituraa do arquivo, o programa é finalizado com um código de
        erro 1.

        Se houver um erro de formatação de data ou se houver uma coluna ausente, o
        programa é finalizado com um código de erro 1.

        Returns:
            None: Nenhum valor é retornado.
        """
        filter_start_date, filter_end_date = datetime_treat(
            self.start_date, self.end_date)
        try:
            with open(self._data_path, mode='r', newline='', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    try:
                        product = row.get('produto', 'Unknown').strip()
                        quantity_str = row.get('quantidade', '').strip()
                        price_str = row.get('preco_unitario', '').strip()
                        sale_date_str = row.get('data_venda', '').strip()

                        if not quantity_str or not price_str or not sale_date_str:
                            continue

                        sale_date = parse_date(sale_date_str, self.date_format)

                        if filter_start_date and sale_date and sale_date < filter_start_date:
                            continue
                        if filter_end_date and sale_date and sale_date >= filter_end_date:
                            continue

                        quantity, unit_price = convert_sale_values(
                            quantity_str, price_str)
                        row_sale_value = calculate_sales(quantity, unit_price)

                        new_global_revenue = update_aggregates(
                            product,
                            quantity,
                            row_sale_value,
                            self.global_revenue,
                            self.revenue_per_product,
                            self.quantity_per_product
                        )
                        self.total_global_revenue += new_global_revenue
                    except (ValueError, KeyError) as _err:
                        logging.warning(
                            "Row skipped due to formatting error: %s - Data: %s", _err, row)
                        continue
        except FileNotFoundError:
            logging.error("Error: The file '%s' was not found.",
                          self._data_path)
            sys.exit(1)
        except ValueError as _err:
            logging.error(
                "Error: Date format is incorrect or missing column. %s", _err)
            sys.exit(1)

    def aggregate_results(self) -> Dict[str, Any]:
        """
        Agrega os resultados da leitura do arquivo CSV e retorna um dicionário com as seguintes chaves:
        - report_date: Data e hora da geração do relatório.
        - filter_dates: Dicionário com as datas de início e fim utilizadas no filtro.
        - total_global_revenue: Valor total de todas as vendas.
        - best_selling_product: Dicionário com o produto mais vendido e a quantidade total de unidades vendidas.
        - revenue_per_product: Lista de dicionários com produtos e respectivas receitas.
        """
        best_selling_product = "None"
        best_selling_quantity = 0
        if self.quantity_per_product:
            best_selling_product = max(
                self.quantity_per_product, key=lambda k: self.quantity_per_product[k])
            best_selling_quantity = self.quantity_per_product[best_selling_product]

        sorted_revenue = sorted(
            self.revenue_per_product.items(), key=lambda item: item[1], reverse=True)
        product_revenue_list = parser_to_dict_list(sorted_revenue)

        return {
            "report_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "filter_dates": {"start": self.start_date, "end": self.end_date},
            "total_global_revenue": round(self.total_global_revenue, 2),
            "best_selling_product": {"product": best_selling_product, "quantity": best_selling_quantity},
            "revenue_per_product": product_revenue_list
        }
