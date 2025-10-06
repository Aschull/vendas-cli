from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class Reader(ABC):
    """
    Interface (Classe Base Abstrata) para leitores de dados.
    """
    @abstractmethod
    def process_data(self) -> Dict[str, Any]:
        """
        Método abstrato para ler o arquivo e retornar a lista de dados.
        """

    @abstractmethod
    def set_file_path(self, file_path: str) -> None:
        """Define o caminho do recurso de dados (arquivo, URL, etc.)."""

    @abstractmethod
    def set_date_filters(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> None:
        """Define os filtros de data para o processamento."""
