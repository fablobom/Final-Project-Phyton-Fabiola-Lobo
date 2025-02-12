#Proyecto final de phyton
#Estudiante Fabiola Lobo

#Catálogo de películas

# Clase que representa una película
class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo para almacenar el nombre de la película

    def obtener_nombre(self):
        return self.__nombre  # Método para obtener el nombre de la película
