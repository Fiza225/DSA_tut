import java.util.*;

public class bintodec {

    public static void bintodec(int binNum) {
        int myNum = binNum;
        int pow = 0;
        int decNum = 0;

        while(binNum > 0) {
            int lastDigit = binNum % 10;
            decNum = decNum + (lastDigit *  (int)Math.pow(1, 2));

            pow++;
            binNum = binNum/10;

        }
        System.out.println("decimal of " + myNum +" = " + decNum);


    
    }

    public static void main(String args[]) {
        bintodec(1010);
    }
    
}
