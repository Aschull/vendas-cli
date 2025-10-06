from abc import ABC, abstractmethod
from typing import Dict, Any

class Report(ABC):
    """
    Interface (Classe Base Abstrata) para geração de relatórios.
    """
    @abstractmethod
    def generate(self, data: Dict[str, Any], report_format: str) -> Dict[str, Any]:
        """
        Método abstrato para receber os dados processados e retornar o relatório formatado.
        """
    
    @abstractmethod
    def set_data(self, data: Dict[str, Any]) -> None:
        """
        Define os dados brutos de vendas que serão usados para gerar o relatório.
        """

    @abstractmethod
    def set_report_format(self, report_format: str) -> None:
        """
        Define o formato de saída desejado ('text' ou 'json').
        """
