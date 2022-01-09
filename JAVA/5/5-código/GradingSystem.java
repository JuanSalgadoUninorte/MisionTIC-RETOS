public class GradingSystem {
    protected Student [][] aprendiz;
    Student aprendiz1 = new Student(0.0, 0.0, 0.0, 0.0);
    public double stat1()
    {
        //promedio
        double suma_datos = 0;
        double promedio = 0;
        for(int l = 0; l<aprendiz.length; l++){
            double nota = aprendiz[l][3].getNota();
            suma_datos += nota;
        }
        promedio = suma_datos / aprendiz.length;
        return promedio;
    }
    public Integer stat2()
    {
        //pasado
        Integer regulares=0;
        for(int l = 0; l<aprendiz.length; l++){
            if( (2.5 < aprendiz[l][3].getNota()) && (aprendiz[l][3].getNota() <= 3.5) ){
                regulares++; 
            }
        }
        return regulares;
    }
    public String stat3()
    {
        //materia
        String[] materias = {"historia", "literatura", "biologia"};
        Integer n1= 0, n2=0, n3=0;
        double promedio_materia_uno = 0, promedio_materia_dos =0, promedio_materia_tres = 0;
        String materia_peor_desempeño = "";
        double calificacion = 0, calificacionb =0, calificacioncx =0;
        for(int p = 0; p<aprendiz.length; p++){
            if(aprendiz[p][1].getGenero()==0.0){
                if(aprendiz[p][2].getMateria()==1.0){
                    n1++;
                    calificacion+=aprendiz[p][3].getNota();
                }
                else if(aprendiz[p][2].getMateria()==2.0){
                    n2++;
                    calificacionb+=aprendiz[p][3].getNota();
                }
                else if(aprendiz[p][2].getMateria()==3.0){
                    n3++;
                    calificacioncx+=aprendiz[p][3].getNota();
                }
                promedio_materia_uno = calificacion /n1;
                promedio_materia_dos = calificacionb /n2;
                promedio_materia_tres = calificacioncx /n3;
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
        String mejor_aprendiz_historia = "";
        double nota_mayor = 0;
        String[] nombres = {"armando", "nicolas", "daniel", "maria", "marcela", "alexandra"};
        Integer num_aprendiz = 0;
        for(int t = 0; t<aprendiz.length; t++){
            if(aprendiz[t][2].getMateria()==1.0){
                if(aprendiz[t][3].getNota()>nota_mayor){
                    nota_mayor = aprendiz[t][3].getNota();
                    num_aprendiz = (int) aprendiz[t][0].getNombre()-1;
                }
            }
        }
        mejor_aprendiz_historia= nombres[num_aprendiz];
        return mejor_aprendiz_historia;
    }
}