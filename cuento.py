def escribir_cuento(nuevaLineCuento):
    nombre_archivo = "Cuento.txt"
    try:
        with open(nombre_archivo, 'a') as archivo:  # Abrir el archivo en modo de apendizaje ('a')
            archivo.write(nuevaLineCuento + ' ')
    except Exception as e:
        print(f"Ocurrió un error al abrir o escribir en el archivo: {e}")

def arreglar_cuento():
    nombre_archivo = "Cuento.txt"
    try:
        with open(nombre_archivo, 'r') as archivo:
            palabras = []
            for linea in archivo:
                palabras.extend(linea.split())
                while len(palabras) >= 15:
                    print(" ".join(palabras[:15]))
                    palabras = palabras[15:]
            if palabras:
                print(" ".join(palabras))
    except Exception as e:
        print(f"Ocurrió un error al abrir o leer el archivo: {e}")