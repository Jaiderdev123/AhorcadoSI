import networkx as nx
import matplotlib.pyplot as plt
class Grafo:
    
    def __init__(self):
        self.grafo = {}
    
    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
        else:
            raise ValueError("El vértice ya existe")
        
    def agregar_arista(self, arista):
        origen = arista.obtener_origen()
        destino = arista.obtener_destino()
        if origen not in self.grafo:
            raise ValueError(f"El vértice {origen.obtener_nombre()} no existe")
        if destino not in self.grafo:
            raise ValueError(f"El vértice {destino.obtener_nombre()} no existe")
        self.grafo[origen].append(destino)

    def esta_en_grafo(self, vertice):
        return vertice in self.grafo
    
    def obtener_vertice(self, nombre):
        for vertice in self.grafo:
            if vertice.obtener_nombre() == nombre:
                return vertice
        return print("No se encontró el vértice: ", nombre)

    def obtener_vecinos(self, vertice):
        return self.grafo[vertice]
    
    def dibujar_grafo(self):
        G = nx.DiGraph()
        for origen in self.grafo:
            for destino in self.grafo[origen]:
                G.add_edge(origen.obtener_nombre(), destino.obtener_nombre())
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=15, font_color="black", font_weight="bold", arrows=True)
        plt.show()
    
    def __str__(self):
        todas_aristas = ""
        for origen in self.grafo:
            for destino in self.grafo[origen]:
                todas_aristas += f"{origen.obtener_nombre()} ---> {destino.obtener_nombre()}\n"
        return todas_aristas
    
class Arista:

    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino

    def obtener_origen(self):
        return self.origen
    
    def obtener_destino(self):
        return self.destino
    
    def __str__(self):
        return f"{self.origen.obtener_nombre()} ---> {self.destino.obtener_nombre()}"

class Vertice:
    def __init__(self, nombre):
        self.nombre = nombre

    def obtener_nombre(self):
        return self.nombre
    
    def __str__(self):
        return self.nombre

class Grafo_NoDirijido(Grafo):
    def agregar_arista(self, arista):
        Grafo.agregar_arista(self, arista)
        regresar_arista = Arista(arista.obtener_destino(), arista.obtener_origen())
        Grafo.agregar_arista(self, regresar_arista)

#Ejemplo de funcionamiento
""""
def crear_grafo(grafo):
    g = grafo()
    for n in ('s', 'a', 'b', 'c', 'd', 'e', 'f', 'g','i','x'):
        g.agregar_vertice(Vertice(n))
    g.agregar_arista(Arista(g.obtener_vertice('s'), g.obtener_vertice('a')))
    g.agregar_arista(Arista(g.obtener_vertice('s'), g.obtener_vertice('b')))
    g.agregar_arista(Arista(g.obtener_vertice('s'), g.obtener_vertice('c')))
    g.agregar_arista(Arista(g.obtener_vertice('s'), g.obtener_vertice('d')))
    g.agregar_arista(Arista(g.obtener_vertice('a'), g.obtener_vertice('b')))
    g.agregar_arista(Arista(g.obtener_vertice('a'), g.obtener_vertice('e')))
    g.agregar_arista(Arista(g.obtener_vertice('a'), g.obtener_vertice('g')))
    return g
G1 = crear_grafo(Grafo)
print(G1)
G1.dibujar_grafo()"
"""