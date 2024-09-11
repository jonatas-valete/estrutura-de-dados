class No:
    def __init__(self, idade):
        self.idade = idade
        self.proximo = None
        self.prioridade = 'Padrão'
    def __repr__(self):
        return f'{self.idade}'
        
        
class Fila:
    def __init__(self):
        self.cabeca = None
        self.tail = None
        
    def append(self, idade):
        no = No(idade)
        if not self.cabeca:
            self.cabeca = no
        if self.tail:
            self.tail.proximo = no
        self.tail = no
           # self.cabeca.proximo = self.tail
        #else:   
        if no.idade >= 65:
            no.prioridade = 'urgente'
            if self.cabeca.prioridade == 'urgente':
                no.proximo = self.tail
                self.tail = no
            else:
                no.proximo = self.cabeca
                self.cabeca = no
        else:
            self.tail = no

    def mostrar(self):
        mostrar = []
        while self.cabeca:
            mostrar.append(self.cabeca.idade)
            self.cabeca = self.cabeca.proximo
        return mostrar
        
            
         
        
