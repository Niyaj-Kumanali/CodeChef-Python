// https://www.codechef.com/practice


import java.util.Scanner;
public class CodeChefSST {
    public static void main(String[] args) {
        int token, i=0 ,A, B, resultA, resultB;

        Scanner sc = new Scanner(System.in);

        System.out.println();
        token = sc.nextInt();

        while(i<token){
            A = sc.nextInt();
            B = sc.nextInt();

            resultA = A*100/10;
            resultB = B*100/20;

            if(resultA > resultB){
                System.out.println("FIRST");
            }
            else if(resultA < resultB){
                System.out.println("SECOND");
            }
            else {
                System.out.println("ANY");
            }
            i++;            
        }
    }
}