package BOJ;

import java.util.*;

public class BOJ_1389 {
    static int N;
    static int M;

    static int[][] adjList;
    static boolean[] visited;

    static int answer;
    static int answerMinValue;
    static int[] shortest;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        adjList = new int[N+1][N+1];
        answer = 0;
        answerMinValue = Integer.MAX_VALUE;
        shortest = new int[N+1];
        for(int i=0;i<M;i++){
            int to = sc.nextInt();
            int from = sc.nextInt();
            adjList[from][to] = 1;
            adjList[to][from] = 1;
        } // end input
//        for(int i=1;i<N+1;i++){
//            for(int j=1;j<N+1;j++){
//                System.out.printf("%d ",adjList[i][j]);
//            }
//            System.out.println();
//        }

        Queue<Integer> queue = new LinkedList<>();
        int count =0;
        for(int i=1;i<N+1;i++){
            queue.clear();
            visited = new boolean[N+1];

            queue.add(i);
            visited[i]= true;
            int[] numArr = new int[N+1];
            fillArrayToMax(numArr,i);
            int kevinBacon = 0;
            int inc = 1;
            while(!queue.isEmpty()){
                if(isVisited(visited)) break;
                int size = queue.size();
                for(int s = 0;s<size;s++) {
                    int tempInd = queue.poll();

                    for (int j = 1; j < N + 1; j++) {
                        if (visited[j]) continue;
                        if (adjList[tempInd][j] == 1) {
                            visited[j] = true;
                            queue.add(j);
                            numArr[j] = Math.min(numArr[j], inc);
                        }
                    }

                }
                inc++;

            }
           // System.out.println(i+"번째 ---------------");
           // System.out.println(Arrays.toString(numArr));
            getSumIndex(numArr,i);
        }

        System.out.println(answer);
    }
    public static boolean isVisited(boolean[] visited){
        for(int i=1;i<=N;i++){
            if(!visited[i])
                return false;
        }
        return true;
    }
    public static void fillArrayToMax(int[] arr,int target){
        for(int i=0;i<arr.length;i++){
            if(i==target){
                arr[i]=0;
                continue;
            }

            arr[i]=Integer.MAX_VALUE;
        }
    }

    public static void getSumIndex(int[] arr,int index){
        int sum =0;
        for(int i=1;i<arr.length;i++){
            sum+=arr[i];
        }
        // answer 과의 비교
        if(answerMinValue > sum ){
            answerMinValue = sum;
            answer= index;
        }

    }


}