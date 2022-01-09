public class GradingSystem{
    protected int cantidadDatos;
    protected double [][] datos;
    public String datosRegistro = "";

    public GradingSystem() {
    }

    public GradingSystem(int cantidadDatos, double[][] datos) {
        this.cantidadDatos = cantidadDatos;
        this.datos = datos;
    }

    public double stat1()
    {
        //promedio
        double suma_datos = 0;
        double promedio = 0;
        for(int l = 0; l<cantidadDatos; l++){
            suma_datos+=datos[l][3];
        }
        promedio = suma_datos / cantidadDatos;
        return promedio;
    }

    public Integer stat2()
    {
        //pasado
        Integer contador_regulares=0;
        for(int l = 0; l<cantidadDatos; l++){
            if( (2.5 < datos[l][3]) && (datos[l][3] <= 3.5) ){
                contador_regulares++; 
            }
        }
        return contador_regulares;
    }

    public String stat3()
    {
        //materia
        String[] materias = {"historia", "literatura", "biologia"};
        Integer c1= 0, c2=0, c3=0;
        double promedio_materia_uno = 0, promedio_materia_dos =0, promedio_materia_tres = 0;
        String materia_peor_desempeño = "";
        double notasa = 0, notasb =0, notasc =0;
        for(int p = 0; p<cantidadDatos; p++){
            if(datos[p][1]==0.0){
                if(datos[p][2]==1.0){
                    c1++;
                    notasa+=datos[p][3];
                }
                else if(datos[p][2]==2.0){
                    c2++;
                    notasb+=datos[p][3];
                }
                else if(datos[p][2]==3.0){
                    c3++;
                    notasc+=datos[p][3];
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
    public String stat4(){
        String mejor_estudiante_historia = "";
        double nota_mayor = 0;
        String[] nombres = {"armando", "nicolas", "daniel", "maria", "marcela", "alexandra"};
        Integer num_estudiante = 0;
        for(int t = 0; t<cantidadDatos; t++){
            if(datos[t][2]==1.0){
                if(datos[t][3]>nota_mayor){
                    nota_mayor = datos[t][3];
                    num_estudiante = (int) datos[t][0]-1;
                }
            }
        }
        mejor_estudiante_historia= nombres[num_estudiante];
        return mejor_estudiante_historia;
    }
}