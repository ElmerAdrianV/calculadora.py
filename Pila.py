"""
    Created on Fri Oct 15 20:25:09 2021
    @author: ElmerAdrianV
"""
class Pila:
    def __init__(self):
        self.lista = []
    
    def isEmpty(self):
        return (not self.lista) or (len(self.lista)==0) 
        
    def push(self, data):
        self.lista.append(data)
        
    def pop(self):
        if (self.isEmpty()==False):
            return self.lista.pop(-1)
        
    def peek(self):
        if (self.isEmpty()==False):
            return self.lista[-1]
        
    def size(self):
        return len(self.lista)
    
    def imprime(self):
        for x in self.lista:
            print(x)