// https://www.codechef.com/practice


import java.util.Scanner;

public class CodeChefRCBPLAY {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        for(int i=0; i<t; i++)
        {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = sc.nextInt();

            int winPoint = x+(z*2);
            int DrawPoint = x+(z*1);

            if(winPoint >= y)
                System.out.println("Yes");
            else if(DrawPoint >= y)
                System.out.println("Yes");
            else
                System.out.println("No");

        }
    }
}
