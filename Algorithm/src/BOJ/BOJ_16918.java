package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_16918 {

    public static class Point{
        int x;
        int y;
        public Point(){}
        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    static int R,C,N;
    static int[][] board;

    static boolean[][] isNoneBomb;
    static int time;

    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,-1,1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st= new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        board = new int[R][C];
        time =1;
        for(int i=0;i<R;i++){
            char[] temp = new char[C];
            temp =  br.readLine().toCharArray();
            for(int j =0;j<C;j++){
                if(temp[j]=='.'){
                    board[i][j] = 0;
                }
                else board[i][j] = 1;
            }
        } // end input

        // Edge Case 처리

        while(true){

            if(time >=N) {
                printBoard();
                break;
            }
            // 폭탄 채우면서 , 기존에 있던 폭탄들시간 증가 시키기
            fillBomb();
            time++;

            if(time >=N) {
                printBoard();
                break;
            }
            // 폭탄 폭발하면서, 기존에 있던 폭탄들도 시간 증가 시키기 + 폭탄 검증
            defuseBomb();
            time++;

            if(time >=N) {
                printBoard();
                break;
            }
        }


    }

    public static void defuseBomb() {
       int[][] copy = copyBoard(board);
        isNoneBomb = new boolean[R][C];
       ArrayList<Point> pointList = new ArrayList<>();
        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                if(board[i][j]==2){
                    pointList.add(new Point(i,j));
                }

            }
        }
        isNoneBomb = checkBomb(pointList,isNoneBomb);
        // 폭탄 폭발
        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                if(isNoneBomb[i][j]){
                    board[i][j] =0;
                }
            }
        }




    }

    private static boolean[][] checkBomb(ArrayList<Point> pointList, boolean[][] isNoneBomb) {
        for(Point point : pointList){
           int x = point.x;
           int y= point.y;
           isNoneBomb[x][y] =true;
           for(int d=0;d<4;d++){
               int nextX = x+ dx[d];
               int nextY = y+dy[d];
               if(isValid(nextX,nextY)){
                   isNoneBomb[nextX][nextY]= true; // 폭탄 없다 표시
               }
           }

        }
        return isNoneBomb;
    }

    public static boolean isValid(int x, int y){
        if(x<0 || x>=R || y<0 || y >=C)
            return false;

        return true;
    }

    public static void fillBomb() {

        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                board[i][j]++;
            }
        }
    }
    public static int[][] copyBoard(int[][] board){
        int[][] copy = new int[R][C];
        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                copy[i][j] = board[i][j];
            }
        }
        return copy;
    }

    public static void print(){
        System.out.println("_____"+ time+" 초--------------");
        for(int i=0;i<R;i++){
            System.out.println(Arrays.toString(board[i]));
        }
        System.out.println("________________");

    }
    public static void printBoard(){
        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++) {
                if (board[i][j] > 0) {
                    System.out.printf("%c", 'O');
                } else
                    System.out.printf("%c", '.');
            }
            System.out.println();
        }

    }
}
