"""
services/finance_service.py
Lógica de negócio: filtros, ordenação, cálculos e resumos financeiros.
Utiliza funções de ordem superior (filter, sorted, map) de forma fundamentada.
"""
from models.movimento import Movimento


# =============================================================================
# FILTROS — utilizar filter() com lambda
# =============================================================================

def filtrar_por_tipo(movimentos: list, tipo: str) -> list:
    """
    Filtra movimentos por tipo ('RECEITA' ou 'DESPESA').

    Exemplo de uso de filter():
        list(filter(lambda m: m.tipo == tipo, movimentos))
    """
    # TODO: implementar com filter() e lambda
    pass


def filtrar_por_categoria(movimentos: list, categoria: str) -> list:
    """Filtra movimentos de uma determinada categoria."""
    # TODO: implementar com filter() e lambda
    pass


def filtrar_por_mes(movimentos: list, ano: int, mes: int) -> list:
    """Filtra movimentos de um determinado mês e ano."""
    # TODO: comparar m.data[:7] com f"{ano:04d}-{mes:02d}"
    pass


def filtrar_por_intervalo_valores(movimentos: list, minimo: float, maximo: float) -> list:
    """Filtra movimentos cujo valor está dentro do intervalo [minimo, maximo]."""
    # TODO: implementar com filter() e lambda
    pass


# =============================================================================
# ORDENAÇÃO — utilizar sorted() com key=lambda
# =============================================================================

def ordenar_por_data(movimentos: list, descendente: bool = False) -> list:
    """
    Ordena movimentos por data.

    Exemplo de uso de sorted():
        sorted(movimentos, key=lambda m: m.data, reverse=descendente)
    """
    # TODO: implementar com sorted() e key=lambda
    pass


def ordenar_por_valor(movimentos: list, descendente: bool = True) -> list:
    """Ordena movimentos por valor (descendente por omissão)."""
    # TODO: implementar com sorted() e key=lambda
    pass


# =============================================================================
# CÁLCULOS
# =============================================================================

def calcular_saldo(movimentos: list) -> float:
    """
    Calcula o saldo atual (total receitas - total despesas).

    Returns:
        Saldo atual como float.
    """
    # TODO: somar valores por tipo e subtrair
    pass


def total_por_categoria(movimentos: list) -> dict:
    """
    Agrupa o total de despesas por categoria.

    Returns:
        Dicionário {categoria: total_gasto}.
    """
    # TODO: usar dicionário para agrupar e somar valores por categoria
    pass


def resumo_mensal(movimentos: list, ano: int, mes: int) -> dict:
    """
    Calcula o resumo financeiro de um determinado mês.

    Returns:
        Dicionário com chaves: 'receitas', 'despesas', 'saldo'.
    """
    # TODO: filtrar por mês e calcular totais
    pass


# =============================================================================
# EXPORTAÇÃO — utilizar map()
# =============================================================================

def exportar_para_lista_dicts(movimentos: list) -> list:
    """
    Converte lista de Movimento para lista de dicionários.
    Utiliza map() para transformar cada objeto.

    Exemplo de uso de map():
        list(map(lambda m: m.to_dict(), movimentos))
    """
    # TODO: implementar com map() e lambda
    pass
