import java.util.Scanner;

public class Bijele {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int akings = 1;
        int aqueens = 1;
        int arooks = 2;
        int abishops = 2;
        int aknights = 2;
        int apawns = 8;
        int kings = in.nextInt();
        int queens = in.nextInt();
        int rooks = in.nextInt();
        int bishops = in.nextInt();
        int knights = in.nextInt();
        int pawns = in.nextInt();
        System.out.println(akings-kings);
        System.out.println(aqueens-queens);
        System.out.println(arooks-rooks);
        System.out.println(abishops-bishops);
        System.out.println(aknights-knights);
        System.out.println(apawns-pawns);
    }
}