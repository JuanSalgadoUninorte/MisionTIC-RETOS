public class GradingSystem {
    protected Student [][] Estudiante;
    Student Estudiante1 = new Student(0.0, 0.0, 0.0, 0.0);

    public double stat1()
    {
        //promedio
        double suma_datos = 0;
        double promedio = 0;
        for(int l = 0; l<Estudiante.length; l++){
            double calificacion = Estudiante[l][3].getNota();
            suma_datos += calificacion;
        }
        promedio = suma_datos / Estudiante.length;
        return promedio;
    }

    public Integer stat2()
    {
        //pasado
        Integer contador_regulares=0;
        for(int l = 0; l<Estudiante.length; l++){

            if( (2.5 < Estudiante[l][3].getNota()) && (Estudiante[l][3].getNota() <= 3.5) ){
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
        for(int p = 0; p<Estudiante.length; p++){
            if(Estudiante[p][1].getGenero()==0.0){
                if(Estudiante[p][2].getMateria()==1.0){
                    c1++;
                    notasa+=Estudiante[p][3].getNota();
                }
                else if(Estudiante[p][2].getMateria()==2.0){
                    c2++;
                    notasb+=Estudiante[p][3].getNota();
                }
                else if(Estudiante[p][2].getMateria()==3.0){
                    c3++;
                    notasc+=Estudiante[p][3].getNota();
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
        for(int t = 0; t<Estudiante.length; t++){
            if(Estudiante[t][2].getMateria()==1.0){
                if(Estudiante[t][3].getNota()>nota_mayor){
                    nota_mayor = Estudiante[t][3].getNota();
                    num_estudiante = (int) Estudiante[t][0].getNombre()-1;
                }
            }
        }
        mejor_estudiante_historia= nombres[num_estudiante];
        return mejor_estudiante_historia;
    }

}