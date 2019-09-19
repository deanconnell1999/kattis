import java.util.Scanner;

public class Autori {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String name = in.nextLine();
        String hyphen = "-";
        System.out.print(""+name.charAt(0));
        for(int i=0;i<name.length();i++) {
            if(name.charAt(i)==hyphen.charAt(0)) {
                System.out.print(""+name.charAt(i+1));
            }
        }
    }
}