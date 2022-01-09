public class App {
    public static void main(String[] args) throws Exception {
        SchoolGradingSystem clase = new SchoolGradingSystem();
        clase.loadData();
        System.out.printf("%.2f %n", clase.stat1());
        System.out.println(clase.stat2());
        System.out.println(clase.stat3());
        System.out.println(clase.stat4());
    }
}