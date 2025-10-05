from abc import ABC, abstractmethod
from typing import Dict, Any

class Reader(ABC):
    """
    Interface (Classe Base Abstrata) para leitores de dados.
    """
    @abstractmethod
    def process_data(self) -> Dict[str, Any]:
        """
        Método abstrato para ler o arquivo e retornar a lista de dados.
        """
