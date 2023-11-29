class Biblioteca:
    def __init__(self):
        self.pila_libros = []

    def prestar_libro(self, libro):
        self.pila_libros.append(libro)
        print(f"El libro '{libro}' ha sido prestado.")

    def devolver_libro(self):
        if self.pila_libros:
            libro_devuelto = self.pila_libros.pop()
            print(f"El libro '{libro_devuelto}' ha sido devuelto.")
        else:
            print("No hay libros prestados en la biblioteca.")

    def mostrar_estado(self):
        if self.pila_libros:
            print("Libros prestados:")
            for libro in reversed(self.pila_libros):
                print(f"- {libro}")
        else:
            print("No hay libros prestados en la biblioteca.")

biblioteca = Biblioteca()

biblioteca.prestar_libro("Cien años de soledad")
biblioteca.prestar_libro("Don Quijote de la Mancha")
biblioteca.mostrar_estado()
biblioteca.devolver_libro()
biblioteca.mostrar_estado()