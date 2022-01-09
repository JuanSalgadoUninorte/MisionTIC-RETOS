public class Student {
    private double nombre;
    private double genero;
    private double materia;
    private double nota;
    public Student(double nombre, double genero, double materia, double nota) {
        this.nombre = nombre;
        this.genero = genero;
        this.materia = materia;
        this.nota = nota;
    }
    public double getNombre() {
        return nombre;
    }
    public void setNombre(double nombre) {
        this.nombre = nombre;
    }
    public double getGenero() {
        return genero;
    }
    public void setGenero(double genero) {
        this.genero = genero;
    }
    public double getMateria() {
        return materia;
    }
    public void setMateria(double materia) {
        this.materia = materia;
    }
    public double getNota() {
        return nota;
    }
    public void setNota(double nota) {
        this.nota = nota;
    }
}