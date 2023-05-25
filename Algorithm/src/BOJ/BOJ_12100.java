package BOJ;

import java.util.Scanner;

public class BOJ_12100 {
    static int N;
    static Block[][] board;

    static int[] dirX ={-1,1,0,0};
    static int[] dirY ={0,0,-1,1};
    public static class Block{
        int value;

        boolean isMerged;

        public Block(){}
        public Block(int value){
            this.value = value;
            this.isMerged=false;
        }

    }
    public static void main(String[] args)  {
       Scanner sc = new Scanner(System.in);
       N = sc.nextInt();

        board = new Block[N][N];
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                board[i][j] = new Block(sc.nextInt());
            }
        }
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                System.out.printf("%d ",board[i][j].value);
            }
            System.out.println();
        } //end input

        // 5번동안 재귀시키자

        for(int z=0;z<5;z++){

            moveBoard(0,board); // up
            moveBoard(1,board); // down
            moveBoard(2,board); // left
            moveBoard(3,board); // right

        }


    }

    private static void moveBoard(int d, Block[][] board) {
        int startIndex = 0;
        int endIndex = N-1;
        boolean xIndex = true;

        switch(d){
            case 0:
                break;
            case 1:
                startIndex= N-1;
                endIndex= 0;
                break;
            case 2:
                xIndex= false;
                break;
            case 3:
                startIndex= N-1;
                endIndex= 0;
                xIndex= false;
                break;
        }


        for(int i=0;i<N;i++){

            for(int j=0;j<N;j++){

            }
        }
    }
}
