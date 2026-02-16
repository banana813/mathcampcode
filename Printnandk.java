import java.util.Arrays;
import java.util.Scanner;

public class Printnandk {
    public static void main(String[] args){
        int n;
        int k;
        Scanner scanner = new Scanner(System.in);
        System.out.print("N? ");
        n = scanner.nextInt();
        System.out.print("K? ");
        k = scanner.nextInt();
        int[] currentString = new int[n];
        for(int i = 0; i < currentString.length; i++){
            currentString[i] = 0;
        }
        for(int i = 0; i < currentString.length; i++){
            System.out.print(currentString[i]+", ");
        }  
        System.out.println("");
        int[][] pastStrings = new int[(int)Math.pow(k, n)][n];
        int[] endString = new int[n];
        for(int i = 0; i < endString.length; i++){
            endString[i] = k-1;
        }
        int currentIndex = 0;
        while(currentString != endString){
            pastStrings[currentIndex] = Arrays.copyOf(currentString, currentString.length);
            currentIndex++;                                                                                                                                                                                                                                                            
            int editDigit = 0;
            int[] tempString = Arrays.copyOf(currentString, currentString.length);
            boolean tempStringConfirmed = false;
            while(!tempStringConfirmed){
                if(tempString[editDigit] != k-1){
                    tempString[editDigit]++;
                }else{
                    tempString[editDigit] = 0;
                }                                                                                                                                                                                                                                                                                                                                                                                 
                for(int i = 0; i < tempString.length; i++){
                    //System.out.print(tempString[i]+", ");
                }
                //System.out.println("");                                                                                                                           
                tempStringConfirmed = true;
                for(int i = 0; i < pastStrings.length; i++){
                    if(Arrays.equals(pastStrings[i], tempString)){
                        tempStringConfirmed = false;                                                                                                   
                        //System.out.println("I just set it to false!");
                        //System.out.println("Index on past string: " + i);
                    }
                }        
                if(tempStringConfirmed == false){
                    editDigit++;
                    tempString = currentString;
                }      
                //System.out.println(editDigit);
            }
            currentString = tempString;
            System.out.println("Actua                                                               l official current string: "+ Arrays.toString(currentString));
        }
    }
}                                                                                                                                                                                                                                              