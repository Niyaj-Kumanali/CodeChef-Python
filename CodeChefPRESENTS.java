// https://www.codechef.com/practice


import java.util.Scanner;
class CodeChefPRESENTS {
    public static void main(String[] args) {
        int token, i=0 ,A, resultA;

        Scanner sc = new Scanner(System.in);

        System.out.println();
        token = sc.nextInt();

        while(i<token){
            A = sc.nextInt();
            
            resultA = A/5;
            System.out.println(A-resultA);
            i++;            
        }
    }
}