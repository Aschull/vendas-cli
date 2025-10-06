import pytest
from core.csv_processor import CSVProcessor

def test_process_data_basic(tmp_path):
    csv_content = """produto,quantidade,preco_unitario,data_venda\nCamiseta,2,49.9,2025-01-01\nCalça,1,99.9,2025-01-02\n"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content, encoding='utf-8')

    processor = CSVProcessor(str(csv_file))
    result = processor.process_data()
    assert result['total_global_revenue'] == pytest.approx(199.7)
    assert result['best_selling_product']['product'] in ['Camiseta', 'Calça']
    assert any(item['product'] == 'Camiseta' for item in result['revenue_per_product'])


def test_process_data_with_date_filter(tmp_path):
    csv_content = """produto,quantidade,preco_unitario,data_venda\nCamiseta,2,49.9,2025-01-01\nCalça,1,99.9,2025-01-10\n"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content, encoding='utf-8')

    processor = CSVProcessor(str(csv_file), start_date='2025-01-05', end_date='2025-01-15')
    result = processor.process_data()
    assert result['total_global_revenue'] == pytest.approx(99.9)
    assert result['best_selling_product']['product'] == 'Calça'


def test_process_data_file_not_found():
    with pytest.raises(SystemExit):
        processor = CSVProcessor('arquivo_inexistente.csv')
        processor.process_data()
