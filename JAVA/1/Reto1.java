import java.util.*;
public class reto1 {
    public static void main(String[] args) throws Exception {
        String[] nombres = {"armando", "nicolas", "daniel", "maria", "marcela", "alexandra"};
        String[] materias = {"historia", "literatura", "biologia"};
       Scanner dato = new Scanner(System.in);
       int contador_regulares = 0, c1=0, c2=0, c3=0, num_estudiante = 0; 
       double suma_calificaciones = 0, promedio_calificaciones = 0, promedio_materia_uno = 0, promedio_materia_tres = 0, promedio_materia_dos = 0;
       double estudiante, genero, materia, calificacion, notasa=0, notasb=0, notasc=0;
       double nota_mayor = 0;
       String materia_peor_desempeño="";
       Integer cantidad_estudiantes = dato.nextInt();
       dato.nextLine();
       for(int i = 0; i < cantidad_estudiantes; i++){
           String entrada_bruta = dato.nextLine();
           String [] datos = entrada_bruta.split(" ");
           estudiante = Double.parseDouble(datos[0]);
           genero = Double.parseDouble(datos[1]);
           materia = Double.parseDouble(datos[2]);
           calificacion = Double.parseDouble(datos[3]);
           suma_calificaciones += calificacion;
           if( (2.5 < calificacion) && (calificacion <= 3.5) ){
               contador_regulares++; 
           }
           //Sexo
           if(genero==0.0){
               if(materia==1.0){
                   c1++;
                   notasa+=calificacion;
               }
               else if(materia==2.0){
                   c2++;
                   notasb+=calificacion;
               }
               else if(materia==3.0){
                   c3++;
                   notasc+=calificacion;
               }
               promedio_materia_uno = notasa /c1;
               promedio_materia_dos = notasb /c2;
               promedio_materia_tres = notasc /c3;
           }
           if((promedio_materia_uno<promedio_materia_dos)&&(promedio_materia_uno<promedio_materia_tres)){
               materia_peor_desempeño = materias[0];
           }
           else if((promedio_materia_dos<promedio_materia_uno)&&(promedio_materia_dos<promedio_materia_tres)){
            materia_peor_desempeño = materias[1];
            }else materia_peor_desempeño = materias[2];
           if(materia==1.0){
               if(calificacion>nota_mayor){
                   nota_mayor = calificacion;
                   num_estudiante = (int) estudiante-1;
               }
           }
       }
        dato.close();
        String nombre_estudiante;
        nombre_estudiante = nombres[num_estudiante];
        promedio_calificaciones = suma_calificaciones / cantidad_estudiantes;
        String resultadoPromedio = String.format("%.02f", promedio_calificaciones);
        String replaceResultadoPromedio = resultadoPromedio.replace(',', '.');
        System.out.println(replaceResultadoPromedio);
        System.out.println(contador_regulares);
        System.out.println(materia_peor_desempeño);
        System.out.println(nombre_estudiante);
    }
}
// String resultadoPromedio = String.format("%.02f", pronedio); String replaceResultadoPromedio = resultadoPromedio.replace(',', '.'); System.out.println(replaceResultadoPromedio);