import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;

public class controladorReto3 extends GradingSystem{

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
    
        String datosEnBruto = datosIngresados.getText();
        super.repeticiones = Integer.parseInt(cantidadRepeticiones.getText());
        super.arrayDeLaClase = new double[repeticiones][4];
        String[] data = datosEnBruto.split("\n");
        try {
            for (int i = 0; i < data.length;i++) {
                String[] data2 = data[i].split(" ");
                for(int j = 0; j < 4; j++){
                    super.arrayDeLaClase[i][j] = Double.parseDouble(data2[j]);
                }
            }
            salida.setText(String.format("%.2f %n %d %n %s %n %s",stat1(),stat2(),stat3(),stat4())); 
        } catch (Exception e) {
            System.out.println("error");
        }
    }
}