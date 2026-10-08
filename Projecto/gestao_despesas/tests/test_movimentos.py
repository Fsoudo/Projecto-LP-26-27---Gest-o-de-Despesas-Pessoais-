"""
tests/test_movimentos.py
Testes unitários para as classes Movimento e Carteira.
Executar com: pytest tests/test_movimentos.py -v
"""
import pytest
from models.movimento import Movimento
from models.carteira import Carteira
from models.exceptions import ValorInvalidoError, CategoriaInvalidaError, DataInvalidaError


# =============================================================================
# Fixtures — dados reutilizáveis nos testes
# =============================================================================

@pytest.fixture
def movimento_valido():
    """Retorna um Movimento válido para usar nos testes."""
    return Movimento(
        descricao="Compras supermercado",
        valor=45.50,
        categoria="Alimentação",
        data="2026-10-01",
        tipo="DESPESA"
    )


@pytest.fixture
def carteira_com_movimentos(movimento_valido):
    """Retorna uma Carteira com um movimento já adicionado."""
    c = Carteira()
    c.adicionar_movimento(movimento_valido)
    return c


# =============================================================================
# Testes — Classe Movimento
# =============================================================================

def test_criar_movimento_valido(movimento_valido):
    """Deve criar um Movimento com os atributos corretos."""
    # TODO: verificar que os atributos correspondem aos valores fornecidos
    pass


def test_movimento_gera_id_automatico():
    """Deve gerar um ID único automaticamente se não for fornecido."""
    # TODO: criar dois movimentos e verificar que os IDs são diferentes e não nulos
    pass


def test_movimento_valor_negativo_lanca_excecao():
    """Deve lançar exceção ao criar Movimento com valor negativo."""
    # TODO: usar pytest.raises(ValorInvalidoError)
    pass


def test_movimento_valor_zero_lanca_excecao():
    """Deve lançar exceção ao criar Movimento com valor zero."""
    # TODO: usar pytest.raises(ValorInvalidoError)
    pass


def test_movimento_data_invalida_lanca_excecao():
    """Deve lançar exceção ao fornecer data em formato inválido."""
    # TODO: usar pytest.raises(DataInvalidaError) com data="32-13-2026"
    pass


def test_movimento_tipo_invalido_lanca_excecao():
    """Deve lançar exceção ao fornecer tipo diferente de RECEITA/DESPESA."""
    # TODO: usar pytest.raises(ValueError) com tipo="OUTRO"
    pass


def test_movimento_to_dict_e_from_dict_roundtrip(movimento_valido):
    """to_dict() seguido de from_dict() deve reconstituir o mesmo objeto."""
    # TODO: verificar que movimento_valido == Movimento.from_dict(movimento_valido.to_dict())
    pass


# =============================================================================
# Testes — Classe Carteira
# =============================================================================

def test_adicionar_movimento_aumenta_tamanho(carteira_com_movimentos):
    """Adicionar um movimento deve aumentar o tamanho da carteira."""
    # TODO: verificar len(carteira) == 1
    pass


def test_remover_movimento_existente_retorna_true(carteira_com_movimentos, movimento_valido):
    """Remover um movimento com ID existente deve retornar True."""
    # TODO: remover pelo id e verificar retorno True
    pass


def test_remover_movimento_inexistente_retorna_false():
    """Remover com ID que não existe deve retornar False."""
    # TODO: criar carteira vazia, tentar remover com ID aleatório
    pass


def test_obter_por_id_encontra_movimento(carteira_com_movimentos, movimento_valido):
    """obter_por_id deve retornar o Movimento correto."""
    # TODO: verificar que o movimento retornado tem o mesmo id
    pass


def test_obter_por_id_retorna_none_se_nao_existe():
    """obter_por_id deve retornar None se o ID não existir."""
    # TODO: verificar retorno None com ID inventado
    pass
