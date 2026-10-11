from importlib.metadata import version

__version__ = version("biblia")


class BbError(Exception):
    """Erro esperado, com mensagem pronta para o usuário."""
