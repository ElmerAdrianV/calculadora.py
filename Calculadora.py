"""
    Created on Fri Oct 15 20:15:09 2021
    @author: ElmerAdrianV
"""
from Pila import Pila
class Calculadora:
    #Función que verificar si un string es un operador
    def is_operator(m, self):
        if m=="+" or m=="-"  or m=="*" or m=="/":
            resp = True
        else:
            resp = False
        return resp
    #Función que verificar si un string es un operador o un parentesis
    def is_operator_or_parentheses(m, self):
        if self.is_operator(m) or m=="(" or m==")":
            resp = True
        else:
            resp = False
        return resp
    #Función que separa un string en una lista de tokens individibles: numeros, operadores & paréntesis.
    def tokenizar(cadena,self):
        tokens=[]
        i=0
        n = len(cadena)
        while i < n:
            #Si es un operador o un paréntisis, separa el string de len 1
            if self.is_operator_or_parentheses(cadena[i:i+1]):
                tokens.append(cadena[i:i+1])
                i+=1
            else:
                #Si el string es un numero, identifica que substring contiene el número y lo separa
                f=i
                while f<n and not self.is_operator_or_parentheses(cadena[f:f+1]):
                    f+=1
                tokens.append(cadena[i:f])
                i=f
        return tokens

    #Función que verifica si un lista de tokens tiene validad sintáctica.
    def is_valid(expresion, self):
        #Variable que guarda el número de paréntisis abiertos
        parentesisAbiertos = 0
        #Variable que funcionará como iterador sobre la cadena
        i=0
        #Vriable que guarda la longitud de la lista de tokens
        n=len(expresion)
        #Si la expresion es vacía, se tomará como inválida
        if len(expresion)==0:
            valid =False
        #si el primer elemento es un operador la expresion no es valida
        else:
            valid =  not self.is_operator(expresion[0])
        
        while valid and i<n:
            m=expresion[i]
            if m=="(":
                #Guarda el parantesis 
                parentesisAbiertos+=1
                if i+1<n:
                    # El siguiente de un parentesis abierto solo puede ser un numero o un parentesis abierto
                    valid = (not self.is_operator_or_parentheses(expresion[i+1])) or expresion[i+1]=="("
                else:
                    valid = False
            elif m==")":
                if parentesisAbiertos==0:
                    valid = False
                else:
                    parentesisAbiertos-=1
                    if i+1<n:
                    # El siguiente de un parentesis cerrado solo puede ser un operador
                        valid = self.is_operator(expresion[i+1])
            elif self.is_operator(m):
                if i+1<n:
                    # El siguiente de un operador solo puede ser un numero o un parentesis abierto
                    valid = (not self.is_operator(expresion[i+1])) or expresion[i+1]=="("
                else:
                    #si hay un operador al final la expresion esta mal
                    valid = False
            else:
                if i+1<n:
                    # El siguiente de un número solo puede ser un operador o un parentesis cerrado
                    valid = self.is_operator(expresion[i+1]) or expresion[i+1]==")"
            i+=1
        # Si el while termino de evaluar la lista completa, checa que todos los paréntisis esten cerrados
        if valid:
            valid = parentesisAbiertos==0
        return valid



cadena="*4+3+n4+n1+2"

print(Calculadora.tokenizar(cadena))
print(Calculadora.is_valid(Calculadora.tokenizar(cadena)))







