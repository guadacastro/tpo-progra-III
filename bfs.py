from estructuras import Grafo
from queue import Queue
############################ metodos
def run (s):
    while not cola.empty():
        u = cola.get()
        recorrido_output.append(u)
        
        for v in g.adyacentes(u):
            if not visitados[v]:
                visitados[v] = True
                padre[v] = u
                nivel[v] = nivel[u]+1
                cola.put(v)
                

def distancia_mas_corta_desde_nodo_base(v):
    return nivel[v]

def camino_mas_corto_desde_cualquier_nodo_al_nodo_base(v):
    camino = []
    while v is not None:
        camino.append(v)
        v = padre[v]
        
    camino.reverse()
    print("[+] El camino mas corto desde cualquier nodo hasta el nodo base es:", camino)

############################## programa principal

g = Grafo(direccional = False)
g.inicializar()

g.agregar_vertice("A")
g.agregar_vertice("B")
g.agregar_vertice("C")
g.agregar_vertice("D")
g.agregar_vertice("E")
g.agregar_vertice("F")
g.agregar_vertice("G")
g.agregar_vertice("H")

g.agregar_arista("A", "B", 0)
g.agregar_arista("A", "D", 0)
g.agregar_arista("B", "C", 0)
g.agregar_arista("D", "E", 0)
g.agregar_arista("D", "F", 0)
g.agregar_arista("F", "E", 0)
g.agregar_arista("E", "G", 0)
g.agregar_arista("G", "H", 0)
g.agregar_arista("F", "H", 0)

 
#-------------------------------------------------
visitados = {}
nivel = {} # distancia
padre = {}
recorrido_output = []
cola = Queue()

#inicializamos
for nodo in g.vertices():
    visitados[nodo] = False
    padre[nodo] = None
    nivel[nodo] = -1 # o podria ser infinito

s = "A" # elegimos un nodo base/origen 
visitados[s] = True
nivel[s] = 0
cola.put(s)

run(s)  
print("[+] El recorrido que hace el algoritmo es:",recorrido_output)
print("[+] La distancia mas corta desde el nodo base es de:",distancia_mas_corta_desde_nodo_base("G"))
camino_mas_corto_desde_cualquier_nodo_al_nodo_base("G")