import java.util.Random;

public class Benchmarking{

    private MetodosOrdenamiento metodosOrdenamiento;

    public  Benchmarking(){
        //long inicioMillis = System.currentTimeMillis(); // fecha de referencia
        //long inicioNano = System.nanoTime(); 

        //System.out.println(inicioMillis);
        //System.out.println(inicioNano);

        metodosOrdenamiento = new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatorio(100000);
        Runnable tarea = () -> metodosOrdenamiento.burbujaTradicional(arreglo);

        double tiempoNano = medirConNanoTime(tarea);
        double tiempoMilis = medirConCurrentTime(tarea);

        System.out.println("Tiempo con nanoTime: "+ tiempoNano + " segundos");
        System.out.println("Tiempo con currentTime: "+ tiempoMilis + " segundos");
    }

    private int[] generarArregloAleatorio(int tamano){
        int[] arreglo = new int[tamano];
        Random random = new Random();
        for(int i = 0; i < tamano; i++){
            arreglo[i] = random.nextInt(100000);
        }
        return new int[] {};
    }
    //Tiempo usando nanoTime (en segundos)
    public double medirConNanoTime(Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio)/1000000000.0;
    }
    ////Tiempo usando currentTimeMillis (en segundos)
    public double medirConCurrentTime(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        return (fin - inicio)/1000.0;
    }
}