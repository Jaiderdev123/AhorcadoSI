class Grafo:
    def __init__(self):
        self.nodos = {}
    
    def agregar_nodo(self, estado):
        if estado.palabraoculta not in self.nodos:
            self.nodos[estado.palabraoculta] = []
    
    def agregar_arista(self, estado1, estado2):
        if estado1.palabraoculta in self.nodos and estado2.palabraoculta in self.nodos:
            self.nodos[estado1.palabraoculta].append(estado2)
            self.nodos[estado2.palabraoculta].append(estado1)
    
    def obtener_vecinos(self, estado):
        return self.nodos.get(estado.palabraoculta, [])
    
    def construir_grafo(self, estados):
        for estado in estados:
            self.agregar_nodo(estado)
            for otro_estado in estados:
                if estado != otro_estado and self.son_vecinos(estado, otro_estado):
                    self.agregar_arista(estado, otro_estado)
    
    def son_vecinos(self, estado1, estado2):
        return sum(1 for a, b in zip(estado1.palabraoculta, estado2.palabraoculta) if a != b) == 1