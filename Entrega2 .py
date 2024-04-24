class Menu: #(Nodo)

    def __init__ (self, nombreProducto, categoria, precio, ventas):
        self.nombreProducto = nombreProducto
        self.categoria = categoria
        self.precio = precio
        self.ventas = ventas
        self.izquierda = None
        self.derecha = None


class Arbol:

    def __init__ (self):
        self.raiz = None

    def agregar_recursivo(self, nodo, producto):
        if producto.ventas < nodo.ventas:
            if nodo.izquierda is None:
                nodo.izquierda = producto
            else:
                self.agregar_recursivo(nodo.izquierda, producto)
        else:
            if nodo.derecha is None:
                nodo.derecha = producto
            else:
                self.agregar_recursivo(nodo.derecha, producto)

    def __inorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.nombreProducto)
            self.__inorden_recursivo(nodo.derecha, resultado)

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.ventas == busqueda:
            return nodo
        if busqueda < nodo.ventas:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    # Funciones públicas

    def agregar(self, producto):
        if not self.raiz:
            self.raiz = producto
        else:
            self.agregar_recursivo(self.raiz, producto)

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)


    def MasVendido(self):
        Mas_Vendidos = []
        self.__inorden_recursivo(self.raiz, Mas_Vendidos)
        Mas_Vendidos.reverse()
        return Mas_Vendidos





#=========================================================================================

Comida = Arbol()

Comida.agregar(Menu("Clasica", "Hamburguesa", 12000, 19))
Comida.agregar(Menu("Doble Carne", "Hamburguesa", 16000, 3))
Comida.agregar(Menu("De Pollo", "Hamburguesa", 14000, 12))
Comida.agregar(Menu("Especial", "Hamburguesa", 20000, 14))
Comida.agregar(Menu("Sencillo", "Perros Calientes", 12000, 10))
Comida.agregar(Menu("Americano", "Perros Calientes", 14500, 15))
Comida.agregar(Menu("Extra Bacon", "Perros Calientes", 17000, 27))
Comida.agregar(Menu("Mexicana", "Pizza", 9000, 6))
Comida.agregar(Menu("Hawaiana", "Pizza", 9000, 8))
Comida.agregar(Menu("Pollo Champiñon", "Pizza", 9000, 9))

print(Comida.MasVendido())