import sqlite3

class DiccionarioDB:
    def __init__(self):
        self.conexion = sqlite3.connect("diccionario.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS palabras (palabra TEXT, longitud INTEGER)")
        self.conexion.commit()
    
    def agregar_palabras(self, palabras):
        palabras_con_longitud = [(palabra, len(palabra)) for palabra in palabras]
        self.cursor.executemany("INSERT INTO palabras VALUES (?, ?)", palabras_con_longitud)
        self.conexion.commit()
    
    def obtener_palabras_de_archivo(self, archivo):
        with open(archivo, 'r', encoding='utf-8') as file:
            palabras = [line.strip() for line in file.readlines()]
        return palabras
    
    def listar_palabras(self):
        palabras = self.obtener_palabras_de_archivo('diccionario_bd.txt')
        self.agregar_palabras(palabras)

    def obtener_palabras_por_longitud(self, longitud):
        self.cursor.execute("SELECT palabra FROM palabras WHERE longitud = ?", (longitud,))
        return [fila[0] for fila in self.cursor.fetchall()]
        self.conexion.close()
if __name__ == "__main__":
    db = DiccionarioDB()
    db.listar_palabras()
    db.conexion.close()