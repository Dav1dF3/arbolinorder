class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def recorrido_inorden(nodo):
    if nodo:
        recorrido_inorden(nodo.izquierda)
        print(nodo.valor, end=" ")
        recorrido_inorden(nodo.derecha)

# Ejemplo de uso
# Construyendo el árbol
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)

"""
    1
   / \
  2   3
 / \
4   5
"""

print("Recorrido inorden:")
recorrido_inorden(raiz)