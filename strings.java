import java.util.*;

public class strings {

    public static void printLetters(String str) {
        for(int i=0; i<str.length(); i++) {
            System.out.println(str.charAt(i) + " ");

        }
        System.out.println();
    }
    public static void main(String args[]) {
        //char arr[] = {'a', 'b', 'c', 'd'};
        //String str = "abcd";
        //String str2 = new String("xyz");

        //Strings are IMMUTABLE

        //Scanner sc = new Scanner(System.in);
        //String name;
        //name = sc.nextLine();
        //System.out.println(name);

        String firstName = "Tony";
        String lastName = "Stark";
        String fullName = firstName + " " + lastName;
       

        printLetters(fullName);
    
    }
}