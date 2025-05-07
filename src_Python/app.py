from benchmarking import Benchmarking #Importa solo lo que quiero
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib
import matplotlib.pyplot as plt

#main
if __name__ == "__main__":
    print("Funciona")
    
    metodosOrden = MetodosOrdenamiento()
    benchmark = Benchmarking()
    
    tam = 10000
    tamanios = [500, 1000, 2000]
    resultados = []

    for tam in tamanios:

        arreglo_base = benchmark.build_arreglo(tam)
        
        metodos = {
            "burbuja":metodosOrden.sortByBubble, 
            "seleccion":metodosOrden.sort_selecction
            }
        
        
        for nombre, metodo in metodos.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
            tuplaResultado = (tam,nombre,tiempo)
            resultados.append(tuplaResultado)
            
        for resultado in resultados:
            tam, nombre, tiempo = resultado
            print(f"Tamaño: {tam}, Metodo: {nombre}, Tiempo: {tiempo:.6f} segundos")

    tiempos_por_metodo ={
        "burbuja" : [],
        "seleccion": []
    }

    # Clasificar metodos por tamaño
    for tam, nombre, tiempo in resultados:
       tiempos_por_metodo[nombre].append(tiempo)

    # Crear grafica

    plt.figure(figsize=(10, 6))

    """
    graficar una linea de tiempo para cada metodo 
    x = tamaño
    y = timepo
    """

    for nombre, tiempos in tiempos_por_metodo.items():
        plt.plot(tamanios, tiempos, label=nombre, marker='o')

    # Agregar parametros
    plt.xlabel("tamaño del arreglo")
    plt.ylabel("Tiempos obtenidos")
    plt.title("Comparativa metodos \n Mathias Añazco  -  2025-05-07 8:50")
    plt.legend()
    plt.grid()
    plt.show()
    

    