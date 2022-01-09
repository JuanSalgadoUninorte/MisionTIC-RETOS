public class GradingSystem {
    protected int cantidadRepeticiones;
    protected double [][] arrayDeLaClase;
    public double stat1() {
        double sumaIterativa = 0, promedio = 0;
        for(int a = 0; a < cantidadRepeticiones; a++){
            sumaIterativa += arrayDeLaClase[a][3];
        }
        promedio = sumaIterativa / cantidadRepeticiones;
        return promedio;
    }
    public int stat2() {
        Integer regulares = 0;
        for(int e = 0; e < cantidadRepeticiones; e++){
            if((arrayDeLaClase[e][3] > 2.5) && (arrayDeLaClase[e][3] <= 3.5)){
                regulares++;
            }
        }
        return regulares;
    }
    public String stat3() {
        String[] materias = {"historia", "literatura", "biologia"};
        Integer c1= 0, c2=0, c3=0;
        double promedio_materia_uno = 0, promedio_materia_dos =0, promedio_materia_tres = 0;
        String materia_peor_desempeño = "";
        double notasa = 0, notasb =0, notasc =0;
        for(int p = 0; p<cantidadRepeticiones; p++){
            if(arrayDeLaClase[p][1]==0.0){
                if(arrayDeLaClase[p][2]==1.0){
                    c1++;
                    notasa+=arrayDeLaClase[p][3];
                }
                else if(arrayDeLaClase[p][2]==2.0){
                    c2++;
                    notasb+=arrayDeLaClase[p][3];
                }
                else if(arrayDeLaClase[p][2]==3.0){
                    c3++;
                    notasc+=arrayDeLaClase[p][3];
                }
                promedio_materia_uno = notasa /c1;
                promedio_materia_dos = notasb /c2;
                promedio_materia_tres = notasc /c3;
            }
        }
        if((promedio_materia_uno<promedio_materia_dos)&&(promedio_materia_uno<promedio_materia_tres)){
            materia_peor_desempeño = materias[0];
        }
        else if((promedio_materia_dos<promedio_materia_uno)&&(promedio_materia_dos<promedio_materia_tres)){
         materia_peor_desempeño = materias[1];
         }else materia_peor_desempeño = materias[2];
        return materia_peor_desempeño;
    }
    public String stat4() {
        String mejor_estudiante_historia = "";
        double nota_mayor = 0;
        String[] nombres = {"armando", "nicolas", "daniel", "maria", "marcela", "alexandra"};
        Integer num_estudiante = 0;
        for(int t = 0; t<cantidadRepeticiones; t++){
            if(arrayDeLaClase[t][2]==1.0){
                if(arrayDeLaClase[t][3]>nota_mayor){
                    nota_mayor = arrayDeLaClase[t][3];
                    num_estudiante = (int) arrayDeLaClase[t][0]-1;
                }
            }
        }
        mejor_estudiante_historia= nombres[num_estudiante];
        return mejor_estudiante_historia;
    }    
}