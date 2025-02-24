from grafo import Grafo

class Estado:
    def __init__(self, palabraoculta="_____", letrasingresadas=None, letrasposibles=27, fallospermitidos=8):
        if letrasingresadas is None:
            letrasingresadas = []
        self.palabraoculta = palabraoculta
        self.letrasingresadas = letrasingresadas
        self.letrasposibles = letrasposibles
        self.fallospermitidos = fallospermitidos


    def buscar_estados(self, grafo, estado_inicial):
        estados = [estado_inicial]
        estado_actual = estado_inicial
        for _ in range(3):
            vecinos = grafo.obtener_vecinos(estado_actual)
            if vecinos:
                for vecino in vecinos:
                    if vecino not in estados:
                        estado_actual = vecino
                        estados.append(estado_actual)
                        break
            else:
                break

        return estados

if __name__ == "__main__":
    grafo = Grafo()
    estado_inicial = Estado(palabraoculta="_____", letrasingresadas=[], letrasposibles=27, fallospermitidos=8)
    estado_intermedio1 = Estado(palabraoculta="c___", letrasingresadas=['c'], letrasposibles=26, fallospermitidos=8)
    estado_intermedio2 = Estado(palabraoculta="ca__", letrasingresadas=['c', 'a'], letrasposibles=25, fallospermitidos=8)
    estado_final = Estado(palabraoculta="casa", letrasingresadas=['c', 'a', 's'], letrasposibles=24, fallospermitidos=8)
    estados = [estado_inicial, estado_intermedio1, estado_intermedio2, estado_final]
    grafo.construir_grafo(estados)
    estados_encontrados = estado_inicial.buscar_estados(grafo, estado_inicial)
    print(f"Estado inicial: {estados_encontrados[0].palabraoculta}")
    if len(estados_encontrados) > 1:
        print(f"Estado intermedio 1: {estados_encontrados[1].palabraoculta}")
    if len(estados_encontrados) > 2:
        print(f"Estado intermedio 2: {estados_encontrados[2].palabraoculta}")
    if len(estados_encontrados) > 3:
        print(f"Estado final: {estados_encontrados[3].palabraoculta}")