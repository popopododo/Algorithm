

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int W;
	static int H;
	static int[][] board;
	static int answer;
	static boolean[][] visited;
	static int[][] buildVisit;
//	static int[] dx = { -1,0,1,1,0,-1 };
//	static int[] dy = {0,1,0,-1,-1,-1 };
	
	static int[] dx1 = { -1,-1,0,1,1,0};
	static int[] dy1 = {0,1,1,1,0,-1 };
	
	static int[] dx2 = {-1,-1,0,1,1,0};
	static int[] dy2 = {-1,0,1,0,-1,-1};
	
	public static class Point {
		int x;
		int y;

		public Point() {
		}

		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}

		@Override
		public String toString() {
			return "Point [x=" + x + ", y=" + y + "]";
		}

	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		W = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());
		W += 2;
		H += 2;
		answer = 0;
		board = new int[H][W];
		visited = new boolean[H][W];
		buildVisit = new int[H][W];
		for (int i = 1; i < H - 1; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j < W - 1; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		} // end input

//		for(int i=0;i<H;i++) {
//			System.out.println(Arrays.toString(board[i]));
//		} 

		bfs(new Point(0, 0));
		
		
		System.out.println(answer);
		
	}

	public static void bfs(Point point) {
		int count=0;
		Queue<Point> queue = new LinkedList<>();
		visited[point.x][point.y] = true;
		queue.add(point);
		while (!queue.isEmpty()) {
			//System.out.println(queue);
			Point tempPoint = queue.poll();
			
			int pointX = tempPoint.x;
			int pointY = tempPoint.y;
			for(int d=0;d<6;d++) {
				int nx=0;
				int ny=0;
				if(pointX%2==1) {
					nx = pointX+dx1[d];
					ny= pointY+dy1[d];
					
				}
				else {
					nx = pointX+dx2[d];
					ny= pointY+dy2[d];
				}
				
				if(isVaild(nx,ny)) {
					//System.out.println(tempPoint +" : "+ nx+" "+ny);
					if(board[nx][ny]==0) {
						queue.add(new Point(nx,ny));
						visited[nx][ny]=true;
					}
					if( board[pointX][pointY] == 0 && board[nx][ny]==1) {
						
						buildVisit[nx][ny]++;
						count++;
					}
				}
				
			}
		}
		answer=count;
	}

	private static boolean isVaild(int nx, int ny) {
		if(nx<0 || nx>=H || ny<0 || ny>=W)
			return false;
		if(visited[nx][ny])
			return false;
		
		return true;
	}

}
