from grafo import Grafo, Vertice, Arista

class Estado:
    def __init__(self, palabraoculta, letrasingresadas, letrasposibles, fallospermitidos):
        self.palabraoculta = palabraoculta
        self.letrasingresadas = letrasingresadas
        self.letrasposibles = letrasposibles
        self.fallospermitidos = fallospermitidos
    
    def __str__(self):
        return f"\nPalabra oculta: {self.palabraoculta}\nLetras ingresadas: {self.letrasingresadas}\nLetras posibles: {self.letrasposibles}\nFallos permitidos: {self.fallospermitidos}"