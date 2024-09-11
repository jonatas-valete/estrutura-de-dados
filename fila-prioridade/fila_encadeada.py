class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
    def __repr__(self):
        return f'{valor}'
        

class Fila:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        
    def append(self, valor):
        no = Node(valor)
        if self.cauda:
            self.cauda.proximo = no
        self.cauda = no
        if not self.cabeca:
            self.cabeca = no
    
    def remover(self):
        if not self.cabeca:
            return None
        removido = self.cabeca.valor
        self.cabeca = self.cabeca.proximo
        if not self.cabeca:
            self.cauda = None    
        return removido
        
    def mostrar(self):
        mostrar = []
        while self.cabeca:
            mostrar.append(self.cabeca.valor)
            self.cabeca = self.cabeca.proximo
        return mostrar
        
            
