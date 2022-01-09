import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;

public class sistemaEstadisticoInterfaz extends GradingSystem {

    @FXML
    private Button saveData;

    @FXML
    private TextField nameFieldID;

    @FXML
    private TextField noteField;

    @FXML
    private TextField subjectFieldID;

    @FXML
    private TextField genderField;

    @FXML
    private TextArea enterData;

    @FXML
    private TextArea exitData;

    @FXML
    private Button processData;

    @FXML
    private Button bringData;

    @FXML
    private Button browseDataCD;

    @FXML
    private Button deleteDataCE;

    @FXML
    private TextField nameFieldCE;

    @FXML
    private TextField subjectFieldCE;

    @FXML
    private TextArea datosRepresentados;

    @FXML
    void traerDatos(MouseEvent event) {
        claseConexion conexionPrimaria = new claseConexion();
        String sql = "SELECT * FROM clase";
        try {
            Connection conexionSecundaria = conexionPrimaria.conectar();
            Statement segunda = conexionSecundaria.createStatement();
            ResultSet rsult = segunda.executeQuery(sql);
            ResultSetMetaData rmd = rsult.getMetaData();
            int columnas = rmd.getColumnCount();
            String datosBrutos = "";
            while(rsult.next()){
                super.cantidadDatos++;//iteraccion de datos para luego de procesar
                for(int i=1; i<= columnas; i++){
                    String valorcol = rsult.getString(i);
                    datosBrutos+=valorcol+" ";
                }
                datosBrutos+="\n";
            }
            enterData.setText(datosBrutos);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }

    @FXML
    void consultarRegistro(MouseEvent event) {
        //crear variable de tipo conexion
        claseConexion conexionPrimaria = new claseConexion();
        String resultado = "";
        String nonData = "No se encontraron resultados";
        try{
            Connection conexionSecundaria = conexionPrimaria.conectar();    
            if(!nameFieldCE.getText().equals("") && !subjectFieldCE.getText().equals("") ){
                String sql = "SELECT * FROM clase WHERE nombre =? and materia=?";
                PreparedStatement statementUtilizado = conexionSecundaria.prepareStatement(sql);
                statementUtilizado.setString(1, nameFieldCE.getText());
                statementUtilizado.setString(2, subjectFieldCE.getText());
                ResultSet resutadobuscado = statementUtilizado.executeQuery();

                if(resutadobuscado.next()){
                    resultado+=resutadobuscado.getString("nombre")+" "+ resutadobuscado.getString("sexo")+" "+ resutadobuscado.getString("materia")
                                            +" "+ resutadobuscado.getString("nota")+ "\n";
                    while(resutadobuscado.next()){
                        resultado+=resutadobuscado.getString("nombre")+" "+ resutadobuscado.getString("sexo")+" "+ resutadobuscado.getString("materia")
                                            +" "+ resutadobuscado.getString("nota")+ "\n";
                    }
                    datosRepresentados.setText(resultado);
                }else{datosRepresentados.setText(nonData);}
                conexionSecundaria.close();
            }
            //solo nombre
            if(!nameFieldCE.getText().equals("")){
                String sql = "SELECT * FROM clase WHERE nombre=?";
                PreparedStatement statementUtilizado = conexionSecundaria.prepareStatement(sql);
                statementUtilizado.setString(1, nameFieldCE.getText());
                ResultSet resutadobuscado = statementUtilizado.executeQuery();

                if(resutadobuscado.next()){
                    resultado+=resutadobuscado.getString("nombre")+" "+ resutadobuscado.getString("sexo")+" "+ resutadobuscado.getString("materia")
                                            +" "+ resutadobuscado.getString("nota")+ "\n";
                    while(resutadobuscado.next()){
                        resultado+=resutadobuscado.getString("nombre")+" "+ resutadobuscado.getString("sexo")+" "+ resutadobuscado.getString("materia")
                                            +" "+ resutadobuscado.getString("nota")+ "\n";
                    }
                    datosRepresentados.setText(resultado);
                }else{datosRepresentados.setText(nonData);}
                conexionSecundaria.close();
            }
            //solo materia
            if(!subjectFieldCE.getText().equals("") ){
                String sql = "SELECT * FROM clase WHERE  materia=?";
                PreparedStatement statementUtilizado = conexionSecundaria.prepareStatement(sql);
                statementUtilizado.setString(1, subjectFieldCE.getText());
                ResultSet resutadobuscado = statementUtilizado.executeQuery();

                if(resutadobuscado.next()){
                    resultado+=resutadobuscado.getString("nombre")+" "+ resutadobuscado.getString("sexo")+" "+ resutadobuscado.getString("materia")
                                            +" "+ resutadobuscado.getString("nota")+ "\n";
                    while(resutadobuscado.next()){
                        resultado+=resutadobuscado.getString("nombre")+" "+ resutadobuscado.getString("sexo")+" "+ resutadobuscado.getString("materia")
                                            +" "+ resutadobuscado.getString("nota")+ "\n";
                    }
                    datosRepresentados.setText(resultado);
                }else{datosRepresentados.setText(nonData);}
            }
            //los dos nombre y materia
            

        }catch(SQLException e){
            System.out.println(e.getMessage());
        }

    }
        
    @FXML
    void eliminarRegistro(MouseEvent event) {
        claseConexion conexionPrimaria = new claseConexion();
        String nonData = "No se encontraron resultados";
        try{
            Connection conexionSecundaria = conexionPrimaria.conectar();
            //elimnar registro con nombre y materia
            if(!nameFieldCE.getText().equals("") && !subjectFieldCE.getText().equals("") ){
                String sql = "DELETE FROM clase WHERE nombre=? and materia=?";
                PreparedStatement accion = conexionSecundaria.prepareStatement(sql);
                    accion.setString(1, nameFieldCE.getText());
                    accion.setString(2,subjectFieldCE.getText());
                    int acceso = accion.executeUpdate();
                    if(acceso>0){
                        datosRepresentados.setText("Registro eliminado correctamente");                
                    }else{
                        datosRepresentados.setText(nonData);
                    }
                    conexionSecundaria.close();
            }
            //elimina todo los registro nombre
            if(!nameFieldCE.getText().equals("")){
                String sql = "DELETE FROM clase WHERE nombre=?";
                PreparedStatement accion = conexionSecundaria.prepareStatement(sql);
                    accion.setString(1, nameFieldCE.getText());
                    int acceso = accion.executeUpdate();
                    if(acceso>0){             
                        datosRepresentados.setText("Todos los registro con el nombre se eliminaron");                
                    }else{
                        datosRepresentados.setText(nonData);
                    }
                    conexionSecundaria.close();
                }
            //elimina todo lo registro con materia
            if(!subjectFieldCE.getText().equals("") ){
                String sql = "DELETE FROM clase WHERE materia=?";
                PreparedStatement accion = conexionSecundaria.prepareStatement(sql);
                    accion.setString(1,subjectFieldCE.getText());
                    int acceso = accion.executeUpdate();
                    if(acceso>0){              
                        datosRepresentados.setText("Todos los registro con la materia se eliminaron");                
                    }else{
                        datosRepresentados.setText(nonData);
                    }
            }
        }catch(SQLException e){
            System.out.println(e.getMessage());
        }

    }

    @FXML
    void procesarDatos(MouseEvent event) {
        exitData.setText("");
        String dataMadre = enterData.getText();
        String Matriz[] = dataMadre.split("\n");
        super.datos = new double [super.cantidadDatos][4];
        try {
            for(int i = 1; i<super.cantidadDatos; i++){
                String temporal[] = Matriz[i].split(" ");
                for(int j = 0; j<4; j++){
                    super.datos[i][j] = Double.parseDouble(temporal[j]);
                }
            }
            exitData.setText(String.format("%.2f %n %d %n %s %n %s",stat1(),stat2(),stat3(),stat4())); 
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    @FXML
    void savingProcess(MouseEvent event) {
        claseConexion conexionPrimaria = new claseConexion();
        String sql = "INSERT INTO clase (nombre, sexo, materia, nota) VALUES (?,?,?,?)";
        try {
            Double nombre = 0.0, sexo = 0.0, materia = 0.0;
            Connection conexionSecundaria = conexionPrimaria.conectar();
            String nombreBruto = nameFieldID.getText();
            String materiaBruto = subjectFieldID.getText();
            Double nota = Double.parseDouble(noteField.getText());
            String sexoBruto = genderField.getText();
            if (nombreBruto.equalsIgnoreCase("armando") || nombreBruto.equalsIgnoreCase("1.0")) {
                nombre = 1.0;
            }else if(nombreBruto.equalsIgnoreCase("nicolas") || nombreBruto.equalsIgnoreCase("2.0")){
                nombre = 2.0;
            }else if(nombreBruto.equalsIgnoreCase("daniel") || nombreBruto.equalsIgnoreCase("3.0")){
                nombre = 3.0;
            }else if(nombreBruto.equalsIgnoreCase("maria") || nombreBruto.equalsIgnoreCase("4.0")){
                nombre = 4.0;
            }else if(nombreBruto.equalsIgnoreCase("marcela") || nombreBruto.equalsIgnoreCase("5.0")){
                nombre = 5.0;
            }else if(nombreBruto.equalsIgnoreCase("alexandra") || nombreBruto.equalsIgnoreCase("6.0")){
                nombre = 6.0;
            }

            if (sexoBruto.equalsIgnoreCase("f") || sexoBruto.equalsIgnoreCase("femenino") || sexoBruto.equals("1.0")) {
                sexo = 1.0;
            }else if(sexoBruto.equalsIgnoreCase("m") || sexoBruto.equalsIgnoreCase("masculino") || sexoBruto.equals("0.0")){
                sexo = 0.0;
            }

            if (materiaBruto.equalsIgnoreCase("historia") || materiaBruto.equalsIgnoreCase("1.0")) {
                materia= 1.0;
            }else if(materiaBruto.equalsIgnoreCase("literatura") || materiaBruto.equalsIgnoreCase("2.0")){
                materia = 2.0;
            }else if(materiaBruto.equalsIgnoreCase("biologia") || materiaBruto.equalsIgnoreCase("3.0")){
                materia = 3.0;
            }

            PreparedStatement stmt = conexionSecundaria.prepareStatement(sql);
            stmt.setDouble(1, nombre);
            stmt.setDouble(2, sexo);
            stmt.setDouble(3, materia);
            stmt.setDouble(4, nota);
            stmt.executeUpdate();
            System.out.println("Nota guardada.");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}