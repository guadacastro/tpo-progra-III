from estructuras import Grafo, DiccionarioPrioridad
import math
import json

############################# metodos
def run(g, vertice_origen):
    solucion = {}
    vertices_no_visitados = DiccionarioPrioridad()
    
    for vertice in g.vertices():
        vertices_no_visitados[vertice] = math.inf
        solucion[vertice] = {'distancia':math.inf, 'vertice_anterior':None}
        
    solucion[vertice_origen]['distancia'] = 0
    vertices_no_visitados[vertice_origen] = 0
    
    while len(vertices_no_visitados) > 0:
        distancia_recorrida, vertice = vertices_no_visitados.pop()
        adyacentes = g.adyacentes(vertice)
        
        for adyacente in adyacentes:
            distancia_adyacente = g.peso_arista(vertice, adyacente)
            distancia_desde_origen = distancia_recorrida + distancia_adyacente
            
            if distancia_desde_origen < solucion[adyacente]['distancia']:
                solucion[adyacente]['distancia'] = distancia_desde_origen
                solucion[adyacente]['vertice_anterior'] = vertice
                vertices_no_visitados[adyacente] = distancia_desde_origen
    
    return solucion

##########################programa principal

g = Grafo(direccional=False)

g.inicializar()
g.agregar_vertice('A')
g.agregar_vertice('B')
g.agregar_vertice('C')
g.agregar_vertice('D')
g.agregar_vertice('E')

g.agregar_arista('A', 'D', 1)
g.agregar_arista('A', 'B', 6)
g.agregar_arista('D', 'B', 2)
g.agregar_arista('D', 'E', 1)
g.agregar_arista('E', 'B', 2)
g.agregar_arista('E', 'C', 5)
g.agregar_arista("B", "C", 5)

vertice_origen = "A"
print(json.dumps(run(g, vertice_origen), indent=4))
