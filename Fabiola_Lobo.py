#Proyecto final de phyton
#Estudiante Fabiola Lobo

#Catálogo de películas

# Clase que representa una película
class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo para almacenar el nombre de la película

    def obtener_nombre(self):
        return self.__nombre  # Método para obtener el nombre de la película
import os

class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado

    def obtener_nombre(self):
        return self.__nombre  # Método para obtener el nombre de la película

class CatalogoPeliculas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{nombre}.txt"

        # Si el archivo no existe, lo crea
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'w') as archivo:
                pass  

    def agregar_pelicula(self, pelicula):
        """ Agrega una película al catálogo (archivo de texto). """
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(pelicula.obtener_nombre() + '\n')
        print(f'Pelicula "{pelicula.obtener_nombre()}" agregada correctamente.')

    def listar_peliculas(self):
        """ Lista todas las películas en el catálogo. """
        try:
            with open(self.ruta_archivo, 'r') as archivo:
                peliculas = archivo.readlines()
                if peliculas:
                    print("\nCatálogo de películas:")
                    for pelicula in peliculas:
                        print(f'- {pelicula.strip()}')
                else:
                    print("El catálogo está vacío.")
        except FileNotFoundError:
            print("El catálogo no existe.")

    def eliminar_catalogo(self):
        """ Elimina el archivo del catálogo. """
        try:
            os.remove(self.ruta_archivo)
            print("Catálogo eliminado correctamente.")
        except FileNotFoundError:
            print("El catálogo no existe.")

# Código principal
def main():
    nombre_catalogo = input("Ingrese el nombre del catálogo de películas: ")
    catalogo = CatalogoPeliculas(nombre_catalogo)

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Eliminar catálogo de películas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_pelicula = input("Ingrese el nombre de la película: ")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar_pelicula(pelicula)
        elif opcion == "2":
            catalogo.listar_peliculas()
        elif opcion == "3":
            catalogo.eliminar_catalogo()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
import os

class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado

    def obtener_nombre(self):
        return self.__nombre  # Método para obtener el nombre de la película

class CatalogoPeliculas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{nombre}.txt"

        # Si el archivo no existe, lo crea
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'w') as archivo:
                pass  

    def agregar_pelicula(self, pelicula):
        """ Agrega una película al catálogo (archivo de texto). """
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(pelicula.obtener_nombre() + '\n')
        print(f'Pelicula "{pelicula.obtener_nombre()}" agregada correctamente.')

    def listar_peliculas(self):
        """ Lista todas las películas en el catálogo. """
        try:
            with open(self.ruta_archivo, 'r') as archivo:
                peliculas = archivo.readlines()
                if peliculas:
                    print("\nCatálogo de películas:")
                    for pelicula in peliculas:
                        print(f'- {pelicula.strip()}')
                else:
                    print("El catálogo está vacío.")
        except FileNotFoundError:
            print("El catálogo no existe.")

    def eliminar_catalogo(self):
        """ Elimina el archivo del catálogo. """
        try:
            os.remove(self.ruta_archivo)
            print("Catálogo eliminado correctamente.")
        except FileNotFoundError:
            print("El catálogo no existe.")

# Programa principal
def main():
    nombre_catalogo = input("Ingrese el nombre del catálogo de películas: ")
    catalogo = CatalogoPeliculas(nombre_catalogo)
    
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Eliminar catálogo de películas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre_pelicula = input("Ingrese el nombre de la película: ")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar_pelicula(pelicula)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
