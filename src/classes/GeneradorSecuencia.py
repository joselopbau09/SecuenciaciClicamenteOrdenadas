import random

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0     
    j = 0     
    k = l     

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:

        m = l+(r-l)//2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

class GeneradorSecuencia:

    def __init__(self, tamanoSecuencia) :
        self.tamanoSecuencia = tamanoSecuencia
        self.secuencia = []
        self.creaSecuencia(tamanoSecuencia)
        self.creaSecuenciaCiclica()

    def getSecuencia(self):
        return self.secuencia

    def creaSecuencia (self, tamanoSecuencia):
        secuencia = []
        while (tamanoSecuencia != len(secuencia)):
            numeroGenerado = random.randint(1,100)
            if(numeroGenerado  not in  secuencia):
                secuencia.append(numeroGenerado)
        mergeSort(secuencia,0,len(secuencia)-1)
        self.secuencia = secuencia    

    def creaSecuenciaCiclica(self):
        indiceCiclo = random.randint(0, len(self.secuencia)-1)
        i = 0
        while (i < indiceCiclo):
            j = 0
            auxiliar = []
            auxiliar.append(self.secuencia[j])
            while(j < len(self.secuencia)):
                if (j == len(self.secuencia)-1):
                    self.secuencia[0] = auxiliar.pop(0)    
                else:    
                    auxiliar.append(self.secuencia[j+1])
                    self.secuencia[j+1] = auxiliar.pop(0)
                j += 1
            i += 1        