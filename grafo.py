import networkx as nx
import matplotlib.pyplot as plt
import heapq
from diccionariodb import DiccionarioDB

class Grafo:
    """
    Clase que representa un grafo dirigido.
    Atributos:
    ----------
    grafo : dict
        Diccionario que almacena los vértices y sus aristas adyacentes.
    Métodos:
    --------
    __init__():
        Inicializa un grafo vacío.
    agregar_vertice(vertice):
        Agrega un vértice al grafo.
    agregar_arista(arista):
        Agrega una arista entre dos vértices en el grafo.
    esta_en_grafo(vertice):
        Verifica si un vértice está en el grafo.
    obtener_vertice(nombre):
        Obtiene un vértice por su nombre.
    obtener_vecinos(vertice):
        Obtiene los vecinos de un vértice.
    dibujar_grafo():
        Dibuja el grafo utilizando NetworkX y Matplotlib.
    __str__():
        Devuelve una representación en cadena de todas las aristas del grafo.
    busqueda_primero_mejor(palabra_oculta, letras_disponibles):
        Implementa el algoritmo de búsqueda primero el mejor para adivinar la palabra.
    """
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
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", 
                font_size=15, font_color="black", font_weight="bold", arrows=True, 
                arrowsize=25, arrowstyle='-|>', width=2)
        plt.show()
    
    def __str__(self):
        todas_aristas = ""
        for origen in self.grafo:
            for destino in self.grafo[origen]:
                todas_aristas += f"{origen.obtener_nombre()} ---> {destino.obtener_nombre()}\n"
        return todas_aristas

    def busqueda_primero_mejor(self, palabra_oculta, letras_disponibles):
        """
        Realiza una búsqueda de la mejor letra para adivinar en el juego del ahorcado utilizando la estrategia de búsqueda primero el mejor.
        Args:
            palabra_oculta (str): La palabra oculta con letras adivinadas y guiones bajos para letras no adivinadas.
            letras_disponibles (list): Lista de letras disponibles para adivinar.
        Returns:
            str: La mejor letra para adivinar según la heurística, o None si no hay letras disponibles.
        """
        db = DiccionarioDB()
        
        longitud_palabra = len(palabra_oculta.replace(" ", ""))
        
        patron = palabra_oculta.replace(" ", "")
        
        palabras_candidatas = db.obtener_palabras_por_longitud(longitud_palabra)
        
        palabras_filtradas = []
        for palabra in palabras_candidatas:
            es_candidata = True
            for i, letra in enumerate(patron):
                if letra != '_' and letra != palabra[i]:
                    es_candidata = False
                    break
            if es_candidata:
                palabras_filtradas.append(palabra)
        
        palabras_candidatas = palabras_filtradas
        
        # Si no hay palabras candidatas
        if not palabras_candidatas:
            return letras_disponibles[0] if letras_disponibles else None

        valores_heuristicos = []
        for letra in letras_disponibles:
            valor = self.heuristica(letra, palabras_candidatas)
            heapq.heappush(valores_heuristicos, (-valor, letra))
        if valores_heuristicos:
            _, mejor_letra = heapq.heappop(valores_heuristicos)
            return mejor_letra
        return None

    def heuristica(self, letra, palabras_candidatas):
        """
        Calcula el valor heurístico para una letra dada basado en su frecuencia
        en una lista de palabras candidatas.

        Args:
            letra (str): La letra a evaluar.
            palabras_candidatas (list of str): La lista de palabras candidatas.

        Returns:
            int: La frecuencia de la letra en las palabras candidatas.
        """
        frecuencia_letra = 0
        for palabra in palabras_candidatas:
            frecuencia_letra += palabra.count(letra)
        return frecuencia_letra


class Arista:
    """
    Clase que representa una arista en un grafo.
    Atributos:
    ----------
    origen : Nodo
        El nodo de origen de la arista.
    destino : Nodo
        El nodo de destino de la arista.
    Métodos:
    --------
    __init__(self, origen, destino):
        Inicializa una nueva instancia de la clase Arista con el nodo de origen y el nodo de destino.
    obtener_origen(self):
        Devuelve el nodo de origen de la arista.
    obtener_destino(self):
        Devuelve el nodo de destino de la arista.
    __str__(self):
        Devuelve una representación en cadena de la arista en el formato "origen ---> destino".
    """

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
    """
    Clase que representa un vértice en un grafo.
    Atributos:
    nombre (str): El nombre del vértice.
    Métodos:
    obtener_nombre(): Devuelve el nombre del vértice.
    __str__(): Devuelve el nombre del vértice como una cadena.
    """
    def __init__(self, nombre):
        self.nombre = nombre

    def obtener_nombre(self):
        return self.nombre
    
    def __str__(self):
        return self.nombre

class Grafo_NoDirijido(Grafo):
    def agregar_arista(self, arista):
        super().agregar_arista(arista)
        regresar_arista = Arista(arista.obtener_destino(), arista.obtener_origen())
        super().agregar_arista(regresar_arista)

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
