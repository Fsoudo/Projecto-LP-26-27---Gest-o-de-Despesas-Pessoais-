"""
tests/test_storage.py
Testes unitários para o módulo de persistência (data_manager).
Executar com: pytest tests/test_storage.py -v
"""
import pytest
import os
import json
from models.movimento import Movimento
import storage.data_manager as gestor


# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture
def lista_movimentos():
    """Retorna uma lista com dois movimentos de teste."""
    return [
        Movimento("Salário", 1200.0, "Outros", "2026-10-01", "RECEITA"),
        Movimento("Renda", 400.0, "Habitação", "2026-10-05", "DESPESA"),
    ]


@pytest.fixture
def caminho_temp(tmp_path):
    """Retorna um caminho temporário para o ficheiro JSON de teste."""
    return str(tmp_path / "test_despesas.json")


# =============================================================================
# Testes
# =============================================================================

def test_salvar_e_carregar_dados_roundtrip(lista_movimentos, caminho_temp, monkeypatch):
    """Guardar e depois carregar deve reconstituir os mesmos movimentos."""
    # TODO: monkeypatchar CAMINHO_FICHEIRO, salvar e verificar que carregar retorna os mesmos dados
    pass


def test_carregar_dados_ficheiro_inexistente_retorna_lista_vazia(caminho_temp, monkeypatch):
    """carregar_dados() deve retornar [] se o ficheiro não existir."""
    # TODO: garantir que o ficheiro não existe e verificar retorno []
    pass


def test_carregar_dados_json_corrompido_retorna_lista_vazia(caminho_temp, monkeypatch):
    """carregar_dados() deve retornar [] se o JSON estiver corrompido."""
    # TODO: escrever conteúdo inválido no ficheiro e verificar retorno []
    pass


def test_salvar_dados_cria_ficheiro(lista_movimentos, caminho_temp, monkeypatch):
    """salvar_dados() deve criar o ficheiro JSON no caminho correto."""
    # TODO: verificar que o ficheiro existe após chamar salvar_dados()
    pass
