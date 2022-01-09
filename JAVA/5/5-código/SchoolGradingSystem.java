public class SchoolGradingSystem extends GradingSystem{
    public void loadData(int o, String [] vectorDerivado)
    {
        aprendiz = new Student[o][4];
        for(int p = 0; p<o; p++)
        {
            String vectorA[] = vectorDerivado[p].split(" ");
            for(int l = 0; l < 4; l++){
                double nombre = Double.parseDouble(vectorA[0]);
                double sexo = Double.parseDouble(vectorA[1]);
                double materia = Double.parseDouble(vectorA[2]);
                double nota = Double.parseDouble(vectorA[3]);
                aprendiz[p][l] = new Student(nombre, sexo, materia, nota);
            }
        }
    }
}