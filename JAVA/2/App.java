public class App {
    public static void main(String[] args) throws Exception {
        SchoolGradingSystem estudiantes = new SchoolGradingSystem();
        estudiantes.readData();
        System.out.printf("%.2f %n", estudiantes.question1());
        System.out.println(estudiantes.question2());
        System.out.println(estudiantes.question3());
        System.out.println(estudiantes.question4());
        
    }
}