// https://www.codechef.com/practice


import java.util.Scanner;

public class CodeChefHARDBET {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        for(int i=0; i<t; i++)
        {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();

            if(c<b && c<a)
                System.out.println("Alice");
            else if(c>b && b<a)
                System.out.println("Bob");
            else
                System.out.println("Draw");
        }
    }
}
