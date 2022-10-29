
class Buscador:

    def __init__(self, secuencia):
        self.secuencia = secuencia

    def BBC (self):
        val = self.encuentraIndice(0, len(self.secuencia)-1)
        return val

    def encuentraIndice(self,indiceIzq, indiceDer) -> int:
        if(indiceIzq == indiceDer):
            return indiceIzq
            
        else:
            mitad = (indiceIzq + indiceDer) // 2
            if (self.secuencia[mitad] < self.secuencia[indiceDer]):
                return self.encuentraIndice(indiceIzq, mitad)
            else:
                return self.encuentraIndice(mitad + 1, indiceDer)