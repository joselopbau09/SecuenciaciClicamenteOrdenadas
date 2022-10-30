from classes.Buscador import Buscador
from classes.GeneradorSecuencia import GeneradorSecuencia

def getInt(mensaje, error,min, max):
    while (True):
        print(mensaje)
        val = input()
        if val.isnumeric():
            if (int(val) < min or max < int(val)):
                print(error)
            else:
                return int(val)
        else:
            print(error)

def main():
    tamanoEjemplar = getInt('Ingresa el tamaño del ejemplar(un número entero mayor que cero):', 'Ingresa una opción valida', 1, 2**40)
    secuenciaGenerada = GeneradorSecuencia(tamanoEjemplar)
    elementosGenerados = secuenciaGenerada.creaSecuencia(tamanoEjemplar)
    
    print('Los elementos serán ...')
    print(f'{elementosGenerados}\n')
    print('Se genera el ejemplar')
    
    secuenciaGenerada.creaSecuenciaCiclica()
    secuencia = secuenciaGenerada.getSecuencia()
    print(secuencia)
    
    buscador = Buscador(secuencia)
    indiceSecuencia = buscador.BBC()
    print(f'El índice del menor elemento es: {indiceSecuencia}')
    
    operacionesAritmeticas = buscador.getAritmeticas()
    operacionesAsignacion = buscador.getAsignacion()
    operacionesComparacion = buscador.getComparacion()
    operacionesTotales = operacionesAritmeticas + operacionesAsignacion + operacionesComparacion
    
    print(f'Comparaciones: {operacionesComparacion}')
    print(f'Asignación: {operacionesAsignacion}')
    print(f'Op aritmeticas: {operacionesAritmeticas}')
    print(f'Operaciones totales: {operacionesTotales}')

main()