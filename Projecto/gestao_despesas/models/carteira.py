"""
models/carteira.py
Módulo que define a classe Carteira — gere a coleção de movimentos em memória.
"""
from models.movimento import Movimento
from models.exceptions import MovimentoNaoEncontradoError


class Carteira:
    """
    Gere a coleção de movimentos financeiros em memória.
    Funciona como repositório in-memory de objetos Movimento.
    """

    def __init__(self):
        self._movimentos: list = []

    def adicionar_movimento(self, movimento: Movimento) -> None:
        """Adiciona um movimento à coleção."""
        # TODO: validar que é instância de Movimento e adicionar à lista
        pass

    def listar_movimentos(self) -> list:
        """Retorna uma cópia da lista de todos os movimentos."""
        # TODO: retornar lista de movimentos
        pass

    def obter_por_id(self, id: str):
        """
        Procura um movimento pelo seu ID.
        Retorna o Movimento se encontrado, ou None caso contrário.
        """
        # TODO: percorrer a lista com ciclo for e retornar o movimento com o id correspondente
        pass

    def remover_movimento(self, id: str) -> bool:
        """
        Remove um movimento pelo ID.
        Retorna True se removido com sucesso, False se o ID não existir.
        """
        # TODO: encontrar e remover o movimento; retornar True/False
        pass

    def atualizar_movimento(self, id: str, **campos) -> bool:
        """
        Atualiza um ou mais campos de um movimento existente.
        Retorna True se atualizado, False se não encontrado.
        """
        # TODO: encontrar o movimento e aplicar os campos fornecidos
        pass

    def __len__(self) -> int:
        return len(self._movimentos)
