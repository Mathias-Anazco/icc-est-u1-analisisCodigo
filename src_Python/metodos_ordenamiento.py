class MetodosOrdenamiento:
    def sortByBubble(self,arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i+1,n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]

        return arreglo
    
    def sort_selecction(self,arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n-1):
            minIndex = i
            for j in range(i+1,n):
                if arreglo[j] < arreglo[minIndex]:
                    minIndex = j
            arreglo[minIndex], arreglo[i] = arreglo[i], arreglo[minIndex]
        return arreglo
        