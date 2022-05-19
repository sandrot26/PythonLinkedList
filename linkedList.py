
#Se crea clase de Nodo.
from ast import Return


class Node:

    def __init__(self,Value):
        #Value se determina el valor.
        self.Value = Value
        #El next es para que pase el valor al siguiente nodo.
        self.Next = None

    def __str__(self):
        #Devuelve el valor en forma de STR.
        return str(self.Value)

#Se crea la clase de LinkedList.
class LinkedList:

    def __init__(self):
        #informacion que tiene la LinkedList sobre la lista.
        self.First = None
        #longitud de la lista.
        self.Size = 0

    #funcion para a;adir a la lista.
    def Append(self, Value):
        #Se determina Valor del Nodo.
        MyNode = Node(Value)

        #Se crea logica del nodo
        if self.Size == 0:
            self.First =MyNode
        
        else:
            #Se recorre toda la linkedlist hasta conseguir el valor None.
            Current = self.First

            while Current.Next != None:
                Current = Current.Next
            #Se repite hasta que el siguiente nodo sea = a None
            Current.Next = MyNode

        #Se define tama;o de la lista
        self.Size += 1 

        return MyNode
    
    #Funcion para eliminar valor de la linkedlist.
    def Remove(self, Value):
        #se determina que si la longitud de la lista es 0, regrese el valor de falso
        
        if self.Size == 0:
            return False

        else:
            Current = self.First
            #Si el Valor es diferente a lo que buscamos, seguira avanzando.
            
            try:
                while Current.Next.Value != Value:
                    Current = Current.Next
                    DeletedNode = Current.Next
                    Current.Next = DeletedNode.Next

            except AttributeError:
                return False

        #restar longitud de la lista.
        self.Size -= 1

        #retornar nodo eliminado.
        return DeletedNode
                
    #Devuelve longitud de la lista.                
    def __len__(self):
        return self.Size

    def __str__(self):
        String = '[ '
        Current = self.First

        for i in range(len(self)):
            String += str(Current)
            if i != len(self) - 1:
                String += str(', ')
            Current = Current.Next
        String += ' ]'

        return String