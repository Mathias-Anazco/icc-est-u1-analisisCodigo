import random
import time
from metodos_ordenamiento import MetodosOrdenamiento
class Benchmarking():
    def __init__(self):#Constructor
        print('Bench Inicializado')
    
    def ejemplo(self):
        arreglo = self.build_arreglo(1000)
        self.mOrdenamiento = MetodosOrdenamiento()
        
        tarea = lambda: self.mOrdenamiento.sortByBubble(arreglo)
        tiempoMillis = self.contar_con_current_time_miles(tarea)
        tiempoNano = self.contar_con_nano_time(tarea)
        print('Tiempo de ejecucion con current_time_millis: ', tiempoMillis, 'ms ')
        print('Tiempo de ejecucion con nano_time: ', tiempoNano, 'ns ')
        
    def build_arreglo(self, size):
        array = []
        for i in range(size):
            numero = random.randint(1, 100000)
            array.append(numero)
        return array
    
    # import time
    # ejecutar tarea tarea()
    def contar_con_current_time_miles(self,tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return (fin - inicio)

        
    def contar_con_nano_time(self,tarea):
        inicio = time.perf_counter()
        tarea()
        fin = time.perf_counter()
        return (fin - inicio)/1000000000
    
    def medir_tiempo(self,tarea,array):
        inicio = time.perf_counter()
        tarea(array)
        fin = time.perf_counter()
        return fin - inicio