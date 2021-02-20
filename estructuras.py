from heapq import heapify, heappush, heappop

class Grafo:
    def __init__(self, direccional=False):
        self.direccional = direccional
    

    def inicializar(self):
        self.__vertices = {}


    def agregar_vertice(self, vertice):
        if vertice not in self.__vertices:
            self.__vertices[vertice] = {}
          

    def eliminar_vertice(self, vertice):
        if vertice in self.__vertices:
            del self.__vertices[vertice]
    

    def vertices(self):
        return list(self.__vertices.keys())
    

    def agregar_arista(self, vertice_origen, vertice_destino, peso):
        if vertice_origen in self.__vertices and vertice_destino in self.__vertices:
            self.__vertices[vertice_origen][vertice_destino] = peso
            
            if not self.direccional:
                self.__vertices[vertice_destino][vertice_origen] = peso

    
    def eliminar_arista(self, vertice_origen, vertice_destino):
        if self.existe_arista(vertice_origen, vertice_destino):
            del self.__vertices[vertice_origen][vertice_destino]
            
            if not self.direccional:
                del self.__vertices[vertice_destino][vertice_origen]
    

    def existe_arista(self, vertice_origen, vertice_destino):
        existe_origen = vertice_origen in self.__vertices
        return existe_origen and vertice_destino in self.__vertices[vertice_origen]
    

    def peso_arista(self, vertice_origen, vertice_destino):
        if self.existe_arista(vertice_origen, vertice_destino):
            return self.__vertices[vertice_origen][vertice_destino]
    

    def adyacentes(self, vertice):
        if vertice in self.__vertices:
            return self.__vertices[vertice]



class DiccionarioPrioridad(dict):
    def __init__(self, *args, **kwargs):
        super(DiccionarioPrioridad, self).__init__(*args, **kwargs)
        self.__recrear_heap()


    def __recrear_heap(self):
        self.__heap = [(priority, key) for key, priority in self.items()]
        heapify(self.__heap)


    def pop(self):
        heap = self.__heap
        priority, key = heappop(heap)
        
        while key not in self or self[key] != priority:
            priority, key = heappop(heap)
        
        del self[key]
        
        return priority, key


    def __setitem__(self, key, priority):
        super(DiccionarioPrioridad, self).__setitem__(key, priority)
        
        if len(self.__heap) < 2 * len(self):
            heappush(self.__heap, (priority, key))
        else:
            self.__recrear_heap()


    def update(self, *args, **kwargs):
        super(DiccionarioPrioridad, self).update(*args, **kwargs)
        self.__recrear_heap()