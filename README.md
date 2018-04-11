# 21
class Nodo_n:
    def __init__ (self, valor, hijos=[]):
        self.valor=valor
        self.hijos=hijos

def buscar(arbol,valor):
    if arbol==None:
        return False
    if arbol.valor==valor:
        return True
    return buscar_hijos(arbol.hijos,valor)

def buscar_hijos(lista,valor):
    if lista==[]:
        return False
    return buscar(lista[0],valor) or buscar_hijos(lista[1:],valor)

def insertar (arbol,valor):
    if arbol==None:
        return Nodo(valor)
    if valor<arbol.valor:
        return Nodo(arbol.valor,insertar(arbol.izquierda,valor),arbol.derecha)
    return Nodo(arbol.valor,arbol.izquierda,insertar(arbol.derecha,valor))

def buscarX(lista):
     for x in range(len(laberinto)):
        for y in range(len(laberinto[x])):
             if "x" in str(laberinto[x][y]) :
                return [x,y]

def buscarCeros(lista,lista2):
    if lista
            

salida = []
with open('archivo.txt', 'r') as f:
    laberinto = [linea.split() for linea in f]



print(buscarX(laberinto))
