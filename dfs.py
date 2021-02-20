from estructuras import Grafo

############################ metodos
def run(u):
    global time
    color[u] = "gris"
    tiempo_recorrido[u][0] = time
    output.append(u)
    time += 1
    
    for x in g.adyacentes(u):
        if color[x] == "blanco":
            padre[x] = u
            run(x)
    
    color[u] = "negro"
    tiempo_recorrido[u][1] = time
    time += 1


############################## programa principal

color = {}  # blanco gris negro
padre = {}
tiempo_recorrido = {}  # [principio, final]
output = []
time = 0 


g = Grafo(direccional=True)

g.inicializar()
g.agregar_vertice("A")
g.agregar_vertice("B")
g.agregar_vertice("C")
g.agregar_vertice("D")
g.agregar_vertice("E")
g.agregar_vertice("F")

g.agregar_arista("A", "B", 0)
# g.agregar_arista("A","C",0)
g.agregar_arista("B", "D", 0)
g.agregar_arista("B", "E", 0)
# g.agregar_arista("E","F",0)
g.agregar_arista("C", "F", 0)
# g.agregar_arista("C","B",0)

#inicializamos todos los vertices en color blanco
for nodo in g.vertices():
    color[nodo] = "blanco"
    padre[nodo] = None
    tiempo_recorrido[nodo] = [-1, -1]

# por si ya se termino de recorrer un grafo y faltan otros que estaban separados
for u in g.vertices():
    if color[u] == "blanco":
        run(u)
        
#mostrando las soluciones    
print("[+] Recorrido:\n")
print("->", output, "\n")
print("[+] Tiempo del recorrido:\n")

for nodo in g.vertices():
    print(nodo, "->", tiempo_recorrido[nodo])

print("\n[+] Padres:\n")

for i in g.vertices():
    print(i, "->", padre[i])
