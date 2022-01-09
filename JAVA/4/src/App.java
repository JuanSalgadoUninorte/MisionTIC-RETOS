import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class App extends Application{
    public static void main(String[] args) throws Exception {
        launch(args);
    }

    @Override
    public void start(Stage arg0) throws Exception {
        FXMLLoader instancia = new FXMLLoader(getClass().getResource("sistemaEstadisticoFormulario.fxml"));
        Parent cargada = instancia.load();
        Scene formularioCargado = new Scene(cargada);
        arg0.setTitle("Reto 4");
        arg0.setScene(formularioCargado);
        arg0.show();
    }
}
