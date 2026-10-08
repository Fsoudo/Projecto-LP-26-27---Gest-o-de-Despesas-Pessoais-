"""
ui/cli.py
Interface de linha de comandos (CLI) da aplicação.
Ponto único de interação com o utilizador — apresenta menus, lê inputs e
chama os serviços e a carteira conforme necessário.
"""
from models.carteira import Carteira
from models.movimento import Movimento
from models.exceptions import ValorInvalidoError, CategoriaInvalidaError, DataInvalidaError
import services.finance_service as servico
import storage.data_manager as gestor


class CLI:
    """Gere o ciclo principal da interface de linha de comandos."""

    def __init__(self):
        self.carteira = Carteira()
        self._carregar_dados()

    # -------------------------------------------------------------------------
    # Ciclo principal
    # -------------------------------------------------------------------------

    def iniciar(self) -> None:
        """Inicia o loop principal da aplicação."""
        # TODO: mostrar menu principal em loop até o utilizador escolher sair
        pass

    def _mostrar_menu_principal(self) -> None:
        """Apresenta o menu principal no terminal."""
        # TODO: imprimir as opções do menu
        # 1. Adicionar movimento
        # 2. Listar todos os movimentos
        # 3. Pesquisar / Filtrar
        # 4. Ordenar movimentos
        # 5. Atualizar movimento
        # 6. Remover movimento
        # 7. Ver resumo / Saldo atual
        # 8. Ver totais por categoria
        # 0. Sair
        pass

    # -------------------------------------------------------------------------
    # Ações do menu
    # -------------------------------------------------------------------------

    def _adicionar_movimento(self) -> None:
        """Solicita dados ao utilizador e adiciona um novo movimento."""
        # TODO: pedir descricao, valor, categoria, data, tipo
        # Usar _pedir_float() e _pedir_data() para validação
        # Tratar exceções e mostrar mensagens de erro amigáveis
        pass

    def _listar_movimentos(self) -> None:
        """Lista todos os movimentos em formato de tabela."""
        # TODO: obter lista da carteira e imprimir com tabulate()
        pass

    def _menu_filtros(self) -> None:
        """Sub-menu de pesquisa e filtragem."""
        # TODO: sub-menu com opções de filtro (categoria, mês, intervalo de valores)
        pass

    def _menu_ordenacao(self) -> None:
        """Sub-menu de ordenação."""
        # TODO: sub-menu com opções de ordenação (por data, por valor)
        pass

    def _atualizar_movimento(self) -> None:
        """Solicita ID e novos valores para atualizar um movimento."""
        # TODO: pedir ID, mostrar movimento atual, pedir novos valores
        pass

    def _remover_movimento(self) -> None:
        """Solicita ID e remove o movimento correspondente."""
        # TODO: pedir ID e confirmar remoção
        pass

    def _mostrar_resumo(self) -> None:
        """Apresenta o saldo atual e resumo financeiro."""
        # TODO: calcular e apresentar saldo, total receitas, total despesas
        pass

    def _mostrar_totais_por_categoria(self) -> None:
        """Apresenta o total de despesas agrupado por categoria."""
        # TODO: chamar servico.total_por_categoria() e apresentar em tabela
        pass

    # -------------------------------------------------------------------------
    # Helpers de validação de input
    # -------------------------------------------------------------------------

    def _pedir_float(self, mensagem: str) -> float:
        """Solicita um número decimal ao utilizador em loop até valor válido."""
        # TODO: usar try/except ValueError em loop while
        pass

    def _pedir_data(self, mensagem: str) -> str:
        """Solicita uma data YYYY-MM-DD ao utilizador em loop até formato válido."""
        # TODO: validar com datetime.strptime em loop while
        pass

    def _pedir_opcao_menu(self, opcoes_validas: list) -> str:
        """Solicita uma opção de menu válida em loop."""
        # TODO: ler input e verificar se está na lista de opções válidas
        pass

    # -------------------------------------------------------------------------
    # Persistência
    # -------------------------------------------------------------------------

    def _carregar_dados(self) -> None:
        """Carrega os movimentos do ficheiro JSON para a carteira."""
        # TODO: chamar gestor.carregar_dados() e adicionar à carteira
        pass

    def _guardar_dados(self) -> None:
        """Persiste os movimentos da carteira no ficheiro JSON."""
        # TODO: chamar gestor.salvar_dados() com a lista da carteira
        pass
