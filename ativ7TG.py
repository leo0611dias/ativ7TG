from abc import ABC, abstractmethod

# Classe Abstrata Base
class Grafo(ABC):
    def __init__(self, vertices):
        self.vertices = vertices

    @abstractmethod
    def adicionar_aresta(self, u, v):
        pass

    @abstractmethod
    def mostrar_grafo(self):
        pass

    # Verifica se o grafo é conexo
    def is_conexo(self):
        visitado = set()

        def dfs(v):
            visitado.add(v)
            for vizinho in self.vizinhos(v):
                if vizinho not in visitado:
                    dfs(vizinho)

        dfs(0)
        return len(visitado) == len(self.vertices)

    # Retorna os vizinhos de um vértice
    @abstractmethod
    def vizinhos(self, v):
        pass

    # Checa se dois grafos são isomorfos (comparação simplificada)
    def is_isomorfo(self, outro):
        if len(self.vertices) != len(outro.vertices):
            return False
        if self.total_arestas() != outro.total_arestas():
            return False
        return sorted([len(self.vizinhos(v)) for v in self.vertices]) == \
               sorted([len(outro.vizinhos(v)) for v in outro.vertices])

    @abstractmethod
    def total_arestas(self):
        pass


# Implementação usando Matriz de Adjacência (Grafo Denso)
class GrafoDenso(Grafo):
    def __init__(self, vertices):
        super().__init__(vertices)
        n = len(vertices)
        self.matriz = [[0] * n for _ in range(n)]

    def adicionar_aresta(self, u, v):
        self.matriz[u][v] = 1
        self.matriz[v][u] = 1  # grafo não direcionado

    def mostrar_grafo(self):
        for linha in self.matriz:
            print(linha)

    def vizinhos(self, v):
        return [i for i, val in enumerate(self.matriz[v]) if val == 1]

    def total_arestas(self):
        return sum(sum(linha) for linha in self.matriz) // 2


# Implementação usando Lista de Adjacência (Grafo Esparso)
class GrafoEsparso(Grafo):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.lista = {v: [] for v in range(len(vertices))}

    def adicionar_aresta(self, u, v):
        self.lista[u].append(v)
        self.lista[v].append(u)

    def mostrar_grafo(self):
        for k, v in self.lista.items():
            print(f"{k}: {v}")

    def vizinhos(self, v):
        return self.lista[v]

    def total_arestas(self):
        return sum(len(v) for v in self.lista.values()) // 2


# ----------------- Testando -----------------
vertices = [0, 1, 2, 3]
g1 = GrafoDenso(vertices)
g2 = GrafoEsparso(vertices)

g1.adicionar_aresta(0, 1)
g1.adicionar_aresta(1, 2)
g1.adicionar_aresta(2, 3)

g2.adicionar_aresta(0, 1)
g2.adicionar_aresta(1, 2)
g2.adicionar_aresta(2, 3)

print("Representação do Grafo Denso:")
g1.mostrar_grafo()
print("O grafo é conexo?", g1.is_conexo())

print("\nRepresentação do Grafo Esparso:")
g2.mostrar_grafo()
print("O grafo é conexo?", g2.is_conexo())

print("\nOs dois grafos são isomorfos?", g1.is_isomorfo(g2))
