import java.sql.*;
public class claseConexion {
    public Connection conectar(){
        String url = "jdbc:sqlite:C:/SQLite/SQLiteStudio/sistemaCalificaciones";
        Connection variableDeConnexion = null;
        try{
            variableDeConnexion = DriverManager.getConnection(url);
        }catch(SQLException e){
            System.out.println(e.getMessage());
        }
        return variableDeConnexion;
    }
}
