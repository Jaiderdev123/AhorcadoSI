from grafo import Grafo, Vertice, Arista
from estado import Estado
if __name__ == "__main__":
    estadoinicial = Estado("____",[],27,8)
    estadointermedio1 = Estado("c___",['c'],26,8)
    estadointermedio2 = Estado("ca_a",['c','a'],25,8)
    estadofinal = Estado("casa",['c','a','s'],24,8)
    g1 = Grafo()
    g1.agregar_vertice(Vertice(estadoinicial))
    g1.agregar_vertice(Vertice(estadointermedio1))
    g1.agregar_vertice(Vertice(estadointermedio2))
    g1.agregar_vertice(Vertice(estadofinal))
    g1.agregar_arista(Arista(g1.obtener_vertice(estadoinicial), g1.obtener_vertice(estadointermedio1)))
    g1.agregar_arista(Arista(g1.obtener_vertice(estadoinicial), g1.obtener_vertice(estadointermedio2)))
    g1.agregar_arista(Arista(g1.obtener_vertice(estadointermedio1), g1.obtener_vertice(estadofinal)))
    g1.agregar_arista(Arista(g1.obtener_vertice(estadointermedio2), g1.obtener_vertice(estadofinal)))
    g1.dibujar_grafo()
    print(g1)