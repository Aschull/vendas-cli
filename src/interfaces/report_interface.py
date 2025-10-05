from abc import ABC, abstractmethod
from typing import Dict, Any

class Report(ABC):
    """
    Interface (Classe Base Abstrata) para geração de relatórios.
    """
    @abstractmethod
    def generate(self) -> Dict[str, Any]:
        """
        Método abstrato para receber os dados processados e retornar o relatório formatado.
        """
