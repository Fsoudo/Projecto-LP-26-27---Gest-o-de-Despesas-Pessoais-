"""
main.py
Ponto de entrada da aplicação Gestão de Despesas Pessoais.
Executar com: python main.py
"""
from ui.cli import CLI


def main():
    """Inicializa e arranca a aplicação."""
    app = CLI()
    app.iniciar()


if __name__ == "__main__":
    main()
