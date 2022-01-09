import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;

public class reto5Controller extends GradingSystem{

    @FXML
    private Button calcular;

    @FXML
    private TextArea salida;

    @FXML
    private TextField cantidadRepeticiones;

    @FXML
    private TextArea datosIngresados;

    @FXML
    void calcularDatosIngresados(MouseEvent event) {

        
        SchoolGradingSystem estudiantes = new SchoolGradingSystem();
        String [] datosEnBruto = datosIngresados.getText().split("\n");
        int repeticiones = Integer.parseInt(cantidadRepeticiones.getText());
        String [] Vector = new String [repeticiones];
        try {
            for (int i = 0; i < repeticiones;i++) {
                Vector[i] = datosEnBruto[i];
            }
            estudiantes.loadData(repeticiones, Vector);
        salida.setText(String.format("%.2f %n %d %n %s %n %s",estudiantes.stat1(),estudiantes.stat2(),estudiantes.stat3(),estudiantes.stat4())); 
        }catch(Exception e) {
            System.out.println("error"+e.getMessage());
        }
    }
}
