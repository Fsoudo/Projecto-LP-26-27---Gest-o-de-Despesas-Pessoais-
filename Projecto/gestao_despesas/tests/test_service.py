"""
tests/test_service.py
Testes unitários para a lógica de negócio (finance_service).
Executar com: pytest tests/test_service.py -v
"""
import pytest
from models.movimento import Movimento
import services.finance_service as servico


# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture
def movimentos_mistos():
    """Lista com receitas e despesas de diferentes categorias e meses."""
    return [
        Movimento("Salário",        1200.0, "Outros",        "2026-10-01", "RECEITA"),
        Movimento("Supermercado",     80.0, "Alimentação",   "2026-10-03", "DESPESA"),
        Movimento("Autocarro",        25.0, "Transporte",    "2026-10-05", "DESPESA"),
        Movimento("Freelance",       300.0, "Outros",        "2026-11-01", "RECEITA"),
        Movimento("Restaurante",      45.0, "Alimentação",   "2026-11-10", "DESPESA"),
    ]


# =============================================================================
# Testes — Filtros
# =============================================================================

def test_filtrar_por_tipo_receitas(movimentos_mistos):
    """Deve retornar apenas os movimentos do tipo RECEITA."""
    # TODO: verificar que todos os elementos retornados têm tipo == "RECEITA"
    pass


def test_filtrar_por_tipo_despesas(movimentos_mistos):
    """Deve retornar apenas os movimentos do tipo DESPESA."""
    # TODO: verificar que todos os elementos retornados têm tipo == "DESPESA"
    pass


def test_filtrar_por_categoria(movimentos_mistos):
    """Deve retornar apenas movimentos da categoria especificada."""
    # TODO: filtrar por "Alimentação" e verificar que são 2
    pass


def test_filtrar_por_mes(movimentos_mistos):
    """Deve retornar apenas movimentos do mês/ano especificado."""
    # TODO: filtrar por outubro 2026 e verificar resultado
    pass


def test_filtrar_por_intervalo_valores(movimentos_mistos):
    """Deve retornar movimentos cujo valor está no intervalo fornecido."""
    # TODO: filtrar entre 30.0 e 100.0 e verificar resultado
    pass


# =============================================================================
# Testes — Ordenação
# =============================================================================

def test_ordenar_por_valor_ascendente(movimentos_mistos):
    """Deve ordenar movimentos por valor crescente."""
    # TODO: verificar que valores estão em ordem crescente
    pass


def test_ordenar_por_valor_descendente(movimentos_mistos):
    """Deve ordenar movimentos por valor decrescente."""
    # TODO: verificar que valores estão em ordem decrescente
    pass


def test_ordenar_por_data(movimentos_mistos):
    """Deve ordenar movimentos por data crescente."""
    # TODO: verificar que datas estão em ordem crescente
    pass


# =============================================================================
# Testes — Cálculos
# =============================================================================

def test_calcular_saldo(movimentos_mistos):
    """Saldo deve ser igual a receitas totais menos despesas totais."""
    # TODO: calcular manualmente e comparar com servico.calcular_saldo()
    pass


def test_total_por_categoria_agrupa_corretamente(movimentos_mistos):
    """total_por_categoria deve agrupar e somar despesas por categoria."""
    # TODO: verificar que "Alimentação" = 80.0 + 45.0 = 125.0
    pass


def test_resumo_mensal_calcula_valores_corretos(movimentos_mistos):
    """resumo_mensal deve retornar receitas, despesas e saldo corretos para o mês."""
    # TODO: verificar resumo de outubro 2026
    pass
