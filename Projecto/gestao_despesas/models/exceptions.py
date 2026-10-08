"""
models/exceptions.py
Exceções personalizadas do domínio da aplicação.
"""


class ValorInvalidoError(Exception):
    """Lançada quando o valor de um movimento é inválido (ex: negativo ou zero)."""
    pass


class CategoriaInvalidaError(Exception):
    """Lançada quando a categoria fornecida não existe na lista de categorias válidas."""
    pass


class MovimentoNaoEncontradoError(Exception):
    """Lançada quando um movimento com o ID fornecido não existe na carteira."""
    pass


class DataInvalidaError(Exception):
    """Lançada quando a data fornecida não está no formato YYYY-MM-DD."""
    pass
