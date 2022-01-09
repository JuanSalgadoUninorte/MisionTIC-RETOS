public class SchoolGradingSystem extends GradingSystem{

    public void loadData(int n, String [] vector)
    {
        Estudiante = new Student[n][4];
        for(int i = 0; i<n; i++)
        {
            String vector1[] = vector[i].split(" ");
            for(int j = 0; j < 4; j++){
                double nombre = Double.parseDouble(vector1[0]);
                double genero = Double.parseDouble(vector1[1]);
                double materia = Double.parseDouble(vector1[2]);
                double nota = Double.parseDouble(vector1[3]);
                Estudiante[i][j] = new Student(nombre, genero, materia, nota);
            }
        }
    }
}