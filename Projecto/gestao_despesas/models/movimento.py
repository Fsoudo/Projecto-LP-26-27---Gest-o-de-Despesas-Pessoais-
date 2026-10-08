"""
models/movimento.py
Módulo que define a classe base Movimento e as suas subclasses/validações.
"""
import uuid
from datetime import datetime


class Movimento:
    """
    Representa um movimento financeiro (receita ou despesa).

    Atributos:
        id (str): Identificador único gerado automaticamente.
        descricao (str): Descrição breve do movimento.
        valor (float): Valor monetário (deve ser positivo).
        categoria (str): Categoria do movimento (ex: Alimentação, Transporte).
        data (str): Data no formato YYYY-MM-DD.
        tipo (str): Tipo do movimento — "RECEITA" ou "DESPESA".
    """

    TIPOS_VALIDOS = ("RECEITA", "DESPESA")
    CATEGORIAS_VALIDAS = {"Alimentação", "Transporte", "Lazer", "Saúde", "Habitação", "Outros"}

    def __init__(self, descricao: str, valor: float, categoria: str,
                 data: str, tipo: str, id: str = None):
        # TODO: Validar cada parâmetro e atribuir aos atributos de instância
        # - id: gerar com str(uuid.uuid4()) se não fornecido
        # - valor: deve ser > 0, caso contrário lançar ValorInvalidoError
        # - tipo: deve estar em TIPOS_VALIDOS, caso contrário lançar ValueError
        # - data: validar com datetime.strptime(data, "%Y-%m-%d"), lançar DataInvalidaError se inválida
        # - categoria: validar contra CATEGORIAS_VALIDAS, lançar CategoriaInvalidaError se inválida
        pass

    def to_dict(self) -> dict:
        """Converte o movimento para dicionário (para serialização JSON)."""
        # TODO: retornar dicionário com todos os atributos
        pass

    @classmethod
    def from_dict(cls, dados: dict) -> "Movimento":
        """Cria um objeto Movimento a partir de um dicionário."""
        # TODO: instanciar Movimento com os valores do dicionário
        pass

    def __str__(self) -> str:
        """Representação legível do movimento para o terminal."""
        # TODO: formatar e retornar string descritiva
        pass

    def __repr__(self) -> str:
        return f"Movimento(id={self.id!r}, tipo={self.tipo!r}, valor={self.valor}, data={self.data!r})"
