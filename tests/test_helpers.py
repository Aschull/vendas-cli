from src.utils import helpers

def test_datetime_treat_valid():
    start, end = helpers.datetime_treat('2025-01-01', '2025-01-05')
    assert start is not None and start.strftime('%Y-%m-%d') == '2025-01-01'
    assert end is not None and end.strftime('%Y-%m-%d') == '2025-01-06'  # inclusivo

def test_datetime_treat_invalid():
    start, end = helpers.datetime_treat('invalid', None)
    assert start is None and end is None

def test_update_aggregates():
    product = 'Camiseta'
    quantity = 2
    sale_value = 100.0
    global_rev = 0.0
    rev_dict = {}
    qty_dict = {}
    new_global = helpers.update_aggregates(product, quantity, sale_value, global_rev, rev_dict, qty_dict)
    assert new_global == 100.0

def test_parser_to_dict_list():
    sorted_revenue = [('Camiseta', 100.0), ('Calça', 50.0)]
    result = helpers.parser_to_dict_list(sorted_revenue)
    assert result == [
        {'product': 'Camiseta', 'revenue': 100.0},
        {'product': 'Calça', 'revenue': 50.0}
    ]

def test_convert_sale_values():
    quantity, price = helpers.convert_sale_values('2', '49.9')
    assert quantity == 2
    assert price == 49.9

def test_calculate_sales():
    assert helpers.calculate_sales(2, 49.9) == 99.8
