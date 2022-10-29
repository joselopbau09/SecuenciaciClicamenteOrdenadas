
class Buscador:

    def __init__(self, secuencia):
        self.secuencia = secuencia
        self.operacionesAritmeticas = 0
        self.operacionesAsignacion = 0
        self.operacionesComparacion = 0

    def getAritmeticas(self):
        return self.operacionesAritmeticas
    
    def getAsignacion(self):
        return self.operacionesAsignacion
    
    def getComparacion(self):
        return self.operacionesComparacion

    def BBC (self):
        val = self.encuentraIndice(0, len(self.secuencia)-1)
        self.operacionesAsignacion += 1
        return val

    def encuentraIndice(self,indiceIzq, indiceDer):
        if(indiceIzq == indiceDer):
            self.operacionesComparacion += 1
            return indiceIzq
            
        else:
            self.operacionesComparacion += 1

            mitad = (indiceIzq + indiceDer) // 2
            self.operacionesAsignacion += 1
            self.operacionesAritmeticas += 1
            if (self.secuencia[mitad] < self.secuencia[indiceDer]):
                self.operacionesComparacion += 1

                return self.encuentraIndice(indiceIzq, mitad)
            else:
                self.operacionesComparacion += 1

                return self.encuentraIndice(mitad + 1, indiceDer)