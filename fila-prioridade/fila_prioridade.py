class No:
    def __init__(self, idade, prioridade='Padrão'):
        self.idade = idade
        self.proximo = None
        self.prioridade = prioridade

    def __repr__(self):
        return f'{self.idade}'
        
        
class Fila:
    def __init__(self):
        self.cabeca = None
        self.atender = []
        #self.tail = None
        
    def append(self, idade, prioridade='Padrão'):
        no = No(idade, prioridade)
        if not self.cabeca:
            self.cabeca = no
        #self.tail = no
        else:
            no.proximo = self.cabeca
            self.cabeca = no

    def ordenar_fila(self):
        mostrar = []
        fila = self.cabeca
        while fila:
            mostrar.append(fila)
            fila = fila.proximo
        fila_ordenada = []
        while mostrar:
            i = mostrar.pop()
            fila_ordenada.append(i)        
        return fila_ordenada

    def mostrar(self):
        pass

    def fila_prioridade(self, fila_ordenada):
        fila_preferencial = []
        fila_padrao = []
        for i in fila_ordenada:
            if i.prioridade == 'Preferencial':
                fila_preferencial.append(i)
            else:
                fila_padrao.append(i)
        return fila_preferencial + fila_padrao

    def atender_fila(self):
        if len(self.atender) == 0:
            pilha = self.ordenar_fila()
            fila = self.fila_prioridade(pilha)
            self.atender = fila
        else:
            del self.atender[0]
            self.atualizar_cabeca()
        return self.atender
        
    def atualizar_cabeca(self):
        self.cabeca = None
        for i in range(len(self.atender)):
            no = No(i)
            if not self.cabeca:
                self.cabeca = no
            else: 
                no.proximo = self.cabeca
                self.cabeca = no            
        
        

     
        
            
