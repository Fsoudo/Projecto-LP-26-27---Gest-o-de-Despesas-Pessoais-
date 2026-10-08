"""
storage/data_manager.py
Módulo responsável pela persistência de dados em ficheiro JSON.
Trata erros de ficheiro inexistente e de JSON corrompido.
"""
import json
import os
from models.movimento import Movimento

CAMINHO_FICHEIRO = "data/despesas.json"


def salvar_dados(movimentos: list) -> None:
    """
    Serializa a lista de movimentos para JSON e guarda no ficheiro.

    Args:
        movimentos: lista de objetos Movimento a guardar.
    """
    # TODO:
    # 1. Garantir que a pasta data/ existe com os.makedirs(exist_ok=True)
    # 2. Converter cada Movimento para dict com to_dict()
    # 3. Escrever o ficheiro com json.dump(..., indent=2, ensure_ascii=False)
    pass


def carregar_dados() -> list:
    """
    Lê o ficheiro JSON e devolve uma lista de objetos Movimento.

    Returns:
        Lista de Movimento carregados do ficheiro.
        Retorna lista vazia se o ficheiro não existir ou estiver corrompido.
    """
    # TODO:
    # 1. Tentar abrir o ficheiro com open()
    # 2. Tratar FileNotFoundError → retornar []
    # 3. Tratar json.JSONDecodeError → imprimir aviso e retornar []
    # 4. Reconstruir objetos com Movimento.from_dict()
    pass
