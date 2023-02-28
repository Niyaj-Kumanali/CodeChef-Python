// https://www.codechef.com/practice

import java.util.Scanner;

public class CodeChefPASSORFAIL {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        
        for(int i=0; i<t; i++)
        {
            int n = sc.nextInt();
            int x = sc.nextInt();
            int p = sc.nextInt();

            int wrongAnswer = n-x;
            int m = (x*3)-wrongAnswer;

            if(m>=p)
                System.out.println("Pass");
            else
                System.out.println("Fail");
        }
    }
}
