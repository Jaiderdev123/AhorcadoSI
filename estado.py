from grafo import Grafo, Vertice, Arista

class Estado:
    """
    Clase que representa el estado del juego del ahorcado.
    Atributos:
    ----------
    palabraoculta : str
        La palabra que el jugador debe adivinar.
    letrasingresadas : list
        Lista de letras que el jugador ha ingresado.
    letrasposibles : list
        Lista de letras que el jugador puede ingresar.
    fallospermitidos : int
        Número de fallos permitidos antes de que el juego termine.
    Métodos:
    --------
    __str__():
        Devuelve una representación en cadena del estado actual del juego.
    """

    def __init__(self, palabraoculta, letrasingresadas, letrasposibles, fallospermitidos):
        self.palabraoculta = palabraoculta
        self.letrasingresadas = letrasingresadas
        self.letrasposibles = letrasposibles
        self.fallospermitidos = fallospermitidos
    
    def __str__(self):
        return f"\nPalabra oculta: {self.palabraoculta}\nLetras ingresadas: {self.letrasingresadas}\nLetras posibles: {self.letrasposibles}\nFallos permitidos: {self.fallospermitidos}"