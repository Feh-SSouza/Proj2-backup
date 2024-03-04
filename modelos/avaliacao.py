class Avaliacao:
    '''Inicializa uma instância de avaliação.
    
    Parâmetros:
    - cliente (str)
    - nota (float)'''
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = float(nota)