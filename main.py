from grafo import Grafo, Vertice, Arista
from estado import Estado

def mostrar_ahorcado(intentos_restantes: int):
    escenas = [
        """
        +---+
            |
            |
            |
           ===""",
        """
        +---+
        O   |
            |
            |
           ===""",
        """
        +---+
        O   |
        |   |
            |
           ===""",
        """
        +---+
        O   |
       /|   |
            |
           ===""",
        """
        +---+
        O   |
       /|\\ |
            |
           ===""",
        """
        +---+
        O   |
       /|\\ |
       /    |
           ===""",
        """
        +---+
        O   |
       /|\\ |
       / \\ |
           ===""",
        """
        +---+
        O   |
      _/|\\ |
       / \\ |
           ===""",
        """
        +---+
       _x_  |
      _/|\\_|
       / \\ |
           ==="""
    ]
    fallos_usados = 9 - intentos_restantes
    if fallos_usados < 0:
        fallos_usados = 0
    if fallos_usados > 9:
        fallos_usados = 9
    print(escenas[fallos_usados])

def main():
    while True:
        palabra = input("Ingrese la palabra a adivinar: ").strip().lower()
        longitud_palabra = len(palabra)
        
    
        estado_inicial = Estado("_" * longitud_palabra, [], 27, 9)
        
    
        g = Grafo()
        g.agregar_vertice(Vertice(estado_inicial))
        
      
        letras_disponibles = list("abcdefghijklmnopqrstuvwxyzáéíóú")
        
        estado_actual = estado_inicial
        
        while "_" in estado_actual.palabraoculta and estado_actual.fallospermitidos > 0:
            mostrar_ahorcado(estado_actual.fallospermitidos)
            mejor_letra = g.busqueda_primero_mejor(estado_actual.palabraoculta, letras_disponibles)
            
            if mejor_letra is None:
                print("No hay más letras disponibles para adivinar.")
                break
            
            letras_disponibles.remove(mejor_letra)
            nueva_palabra_oculta = "".join(
                mejor_letra if palabra[i] == mejor_letra else estado_actual.palabraoculta[i]
                for i in range(longitud_palabra)
            )

            if mejor_letra in palabra:
                nuevos_fallos = estado_actual.fallospermitidos
            else:
                nuevos_fallos = estado_actual.fallospermitidos - 1

            estado_actual = Estado(
                nueva_palabra_oculta,
                estado_actual.letrasingresadas + [mejor_letra],
                estado_actual.letrasposibles - 1,
                nuevos_fallos
            )
            
            nuevo_vertice = Vertice(estado_actual)
            g.agregar_vertice(nuevo_vertice)
            g.agregar_arista(Arista(g.obtener_vertice(estado_inicial), nuevo_vertice))
            
            print(f"Estado actual: {estado_actual.palabraoculta}, Letras ingresadas: {estado_actual.letrasingresadas}, Fallos permitidos: {estado_actual.fallospermitidos}")
        
        if "_" not in estado_actual.palabraoculta:
            print(f"Adiviné la palabra: {estado_actual.palabraoculta}")
        else:
            print(f"No adivine la palabra. La palabra era: {palabra}")
        continuar = input("¿Desea continuar? (s/n): ")
        if continuar.lower() != "s":
            break
if __name__ == "__main__":
    main()