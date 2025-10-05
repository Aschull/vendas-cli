from src.reports.sales_report import SalesReport

def test_generate_report_text_output(capsys):
    data = {
        "report_date": "2025-10-04 12:00:00",
        "filter_dates": {"start": "2025-01-01", "end": "2025-01-10"},
        "total_global_revenue": 149.8,
        "best_selling_product": {"product": "Camiseta", "quantity": 3},
        "revenue_per_product": [
            {"product": "Camiseta", "revenue": 149.8}
        ]
    }
    report = SalesReport(data, report_format='text')
    captured = capsys.readouterr()
    assert "RELATÓRIO DE VENDAS" in captured.out
    assert "Camiseta" in captured.out
    assert "R$ 149.80" in captured.out


def test_generate_report_json_output(capsys):
    data = {
        "report_date": "2025-10-04 12:00:00",
        "filter_dates": {"start": "2025-01-01", "end": "2025-01-10"},
        "total_global_revenue": 149.8,
        "best_selling_product": {"product": "Camiseta", "quantity": 3},
        "revenue_per_product": [
            {"product": "Camiseta", "revenue": 149.8}
        ]
    }
    report = SalesReport(data, report_format='json')
    captured = capsys.readouterr()
    assert '{' in captured.out
    assert '"Camiseta"' in captured.out
    assert '"total_global_revenue": 149.8' in captured.out
