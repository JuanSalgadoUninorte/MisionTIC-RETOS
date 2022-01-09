import java.util.Scanner;
public class SchoolGradingSystem extends GradingSystem{
    
    public void loadData(){
        Scanner input = new Scanner(System.in);
        cantidadRepeticiones = Integer.parseInt(input.nextLine()); 
            arrayDeLaClase = new double[cantidadRepeticiones][4];
            for(int i = 0; i<cantidadRepeticiones; i++)
            {
                String vector[] = input.nextLine().split(" ");
                for(int j = 0; j < 4; j++)
                {
                    //de string a double y de double a arrayDeLaClase
                    arrayDeLaClase[i][j] = Double.parseDouble(vector[j]);
                }
            }
        input.close();
    }
}