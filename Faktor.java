import java.util.Scanner;

public class Faktor {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int articles = in.nextInt();
        double impact = in.nextDouble()-0.99;
        System.out.println((int)((articles*impact)+1));
    }
}