import java.util.Scanner;

public class TakeTwoStones{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        
        int stones = in.nextInt();
        
        if(stones%2!=0){
            System.out.println("Alice");
        }else{
            System.out.println("Bob");
        }
    }
}