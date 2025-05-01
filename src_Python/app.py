#import benchmarking as Ben #Alias Ben
from benchmarking import Benchmarking #Importa solo lo que quiero
from metodos_ordenamiento import MetodosOrdenamiento
#main
if __name__ == "__main__":
    print("Funciona")
    #Ben.Benchmarking()#Archivo.clases
    metodosOrden = MetodosOrdenamiento()
    benchmark = Benchmarking()
    
    tam = 10000
    arreglo_base = benchmark.build_arreglo(tam)
    
    metodos = {
        "burbuja":metodosOrden.sortByBubble, 
        "seleccion":metodosOrden.sort_selecction
        }
    resultados = []
    for nombre, metodo in metodos.items():
        tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
        tuplaResultado = (tam,nombre,tiempo)
        resultados.append(tuplaResultado)
        
    for resultado in resultados:
        tam, nombre, tiempo = resultado
        print(f"Tamaño:{tam}, Metodo: {nombre}, Tiempo: {tiempo:.6f} segundos")