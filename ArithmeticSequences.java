import java.util.ArrayList;
import java.util.Arrays;

public class ArithmeticSequences {
    public static void main(String[] args){
        int goUpTo = 90;
        int[] numIntsToAdd = {6};
        int[] sequenceOneParams = {3, 5};
        int[] sequenceTwoParams = {4, 3};
        int[] sequenceOne = new int[((goUpTo - sequenceOneParams[0])/(sequenceOneParams[1]) + 1)];
        int[] sequenceTwo = new int[((goUpTo - sequenceTwoParams[0])/(sequenceTwoParams[1]) + 1)];
        for(int i = 0; i*sequenceOneParams[1] + sequenceOneParams[0] < goUpTo; i++){
            sequenceOne[i] = i*sequenceOneParams[1] + sequenceOneParams[0];
        }
        for(int i = 0; i*sequenceTwoParams[1] + sequenceTwoParams[0] < goUpTo; i++){
            sequenceTwo[i] = i*sequenceTwoParams[1] + sequenceTwoParams[0];
        }
        System.out.println(Arrays.toString(sequenceOne));
        System.out.println(Arrays.toString(sequenceTwo));
        int[] sequentialSet = new int[sequenceOne.length + sequenceTwo.length + numIntsToAdd.length];
        for(int i = 0; i < sequenceOne.length; i++){
            sequentialSet[i] = sequenceOne[i];
        }
        for(int i = 0; i < sequenceTwo.length; i++){
            sequentialSet[i+sequenceOne.length] = sequenceTwo[i];
        }
        for(int i = 0; i < numIntsToAdd.length; i ++){
            sequentialSet[i + sequenceOne.length + sequenceTwo.length] = numIntsToAdd[i];
        }
        Arrays.sort(sequentialSet);
        System.out.println(Arrays.toString(sequentialSet));
        ArrayList<Integer> complement = new ArrayList<>();
        for(int i = 0; i < 90; i++){
            boolean inSet = Arrays.binarySearch(sequentialSet, i) >= 0;
            if(!inSet){
                complement.add(i);                
            }
        }
        System.out.println(complement);
        ArrayList<int[]> sequenceParams = new ArrayList<int[2]>();
        for(int i = 0; i < complement.size(); i++){
            boolean stepFound = false;
            int upDigit = 0;
            while(!stepFound && upDigit < complement.size() - i){
                upDigit++;
                int difference = 0;
                int oldDifference = 0;
                stepFound = true;
                for(int j = 0; j < (complement.size()-i)/(upDigit+1); j++){
                    if(oldDifference == 0){
                        oldDifference = complement.get(i+upDigit) - complement.get(i);
                    }
                    difference = complement.get(i+(upDigit+1)*j) - complement.get(i+ upDigit*j);
                    if(oldDifference!=difference){
                        stepFound = false;
                        break;
                    }
                    oldDifference = difference;
                }
            }
        }
    }
}
