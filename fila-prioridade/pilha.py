class Item:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        
    def __repr__(self):
        return f'{self.valor}'
        

class Pilha:
    def __init__(self):
        self.topo = None
        
    def push(self, item):
        try:
            v_item = Item(item)
            v_item.anterior = self.topo
            self.topo = v_item
            print(f'{self.topo} adicionado ao topo da pilha')
        except:
          print("ERRO.")
        
    def pop(self):
        if self.topo == None:
            print('lista vazia')
        else:
            self.topo = self.topo.anterior

            
   
stack = Pilha()
stack.push(1)
stack.push(2)
print("Topo da pilha:",stack.topo)
