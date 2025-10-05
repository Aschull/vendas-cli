from datetime import datetime, timedelta
from typing import Dict, Tuple, List, Any, Optional


def datetime_treat(start_date: Optional[str], end_date: Optional[str]) -> Tuple[Optional[datetime], Optional[datetime]]:
    """
    Trata as datas de início e fim fornecidas, convertendo-as para objetos datetime.
    Se as datas forem válidas, retorna um tuple com dois elementos None.
    Se as datas forem inválidas, lança um ValueError.
    Se apenas uma das datas for fornecida, o outro elemento do tuple será None.
    Se a data de fim for fornecida, adiciona 1 dia para tornar o filtro inclusivo.
    Retorna um tuple com dois elementos: o primeiro é a data de início tratada e o segundo é a data de fim tratada.
    """
    date_format: str = "%Y-%m-%d"

    filter_start_date: datetime | None = None
    filter_end_date: datetime | None = None
    try:
        if start_date:
            filter_start_date = datetime.strptime(start_date, date_format)

        if end_date:
            filter_end_date = datetime.strptime(
                end_date, date_format) + timedelta(days=1)

    except ValueError:
        return (None, None)

    return (filter_start_date, filter_end_date)


def update_aggregates(
    product: str,
    quantity: int,
    row_sale_value: float,
    current_global_revenue: float,
    revenue_dict: Dict[str, float],
    quantity_dict: Dict[str, int]
) -> float:
    """
    Atualiza os atributos de receita e quantidade.

    Args:
        product (str): O produto da venda
        quantity (int): A quantidade de produtos vendidos
        row_sale_value (float): O valor da venda
        current_global_revenue (float): O valor total de todas as vendas
        revenue_dict (Dict[str, float]): Um dicionário com a receita por produto
        quantity_dict (Dict[str, int]): Um dicionário com a quantidade por produto

    Returns:
        float: O novo valor total de todas as vendas
    """
    new_global_revenue = current_global_revenue + row_sale_value
    revenue_dict[product] = revenue_dict.get(product, 0.0) + row_sale_value
    quantity_dict[product] = quantity_dict.get(product, 0) + quantity
    return new_global_revenue


def parser_to_dict_list(sorted_revenue: List[Tuple[str, float]]) -> List[Dict[str, Any]]:
    """
    Converte uma lista de tuplas contendo produtos e receitas para uma lista de dicionários.

    Args:
        sorted_revenue (List[Tuple[str, float]]): Uma lista de tuplas contendo produtos e receitas.

    Returns:
        List[Dict[str, Any]]: Uma lista de dicionários com produtos e receitas.
    """
    return [{"product": p, "revenue": round(r, 2)} for p, r in sorted_revenue]


def convert_sale_values(quantity_str: str, price_str: str) -> Tuple[int, float]:
    """
    Converte strings de quantidade e preço para valores numéricos.

    Args:
        quantity_str (str): A string contendo a quantidade de produtos vendidos.
        price_str (str): A string contendo o preço unitário dos produtos.

    Returns:
        Tuple[int, float]: Um tuple contendo a quantidade como um inteiro e o preço unitário como um float.
    """
    quantity = int(quantity_str)
    unit_price = float(price_str.replace(',', '.'))

    return quantity, unit_price


def calculate_sales(quantity: int, unit_price: float) -> float:
    """
    Calcula o valor total de uma venda com base na quantidade e no preço unitário.

    Args:
        quantity (int): A quantidade de produtos vendidos.
        unit_price (float): O preço unitário dos produtos.

    Returns:
        float: O valor total da venda.
    """
    return quantity * unit_price


def parse_date(date_str: str, date_format: str = "%Y-%m-%d") -> Optional[datetime]:
    """
    Parse a date string into a datetime object.

    Args:
        date_str (str): The date string to be parsed.
        date_format (str, optional): The format of the date string. Defaults to "%Y-%m-%d".

    Returns:
        Optional[datetime]: The parsed datetime object, or None if the parsing fails.
    """
    try:
        return datetime.strptime(date_str, date_format)
    except ValueError:
        return None
