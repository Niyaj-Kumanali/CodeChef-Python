// https://www.codechef.com/practice


import java.util.Scanner;
public class CodeChefWATERCOOLER1 {
    public static void main(String[] args) {
        int x, y , t, m;

        Scanner sc = new Scanner(System.in);

        t = sc.nextInt();

        int i=0;
        while(i<t)
        {
            x = sc.nextInt();
            y = sc.nextInt();
            m = sc.nextInt();

            int resultX = x*m;
            int resultY = y;

            if(resultX < resultY)
            {
                System.out.println("YES");
            }
            else
            {
                System.out.println("NO");
            }
            i++;
        }
    }
}
