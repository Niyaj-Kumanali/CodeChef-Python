// https://www.codechef.com/practice

import java.util.Scanner;

public class CodeChefLAZYCHF {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        for(int i=0; i<t; i++)
        {
            int x = sc.nextInt();
            int m = sc.nextInt();
            int d = sc.nextInt();

            if(x*m < x+d)
                System.out.println(x*m);
            else
                System.out.println(x+d);
        }
    }
}
