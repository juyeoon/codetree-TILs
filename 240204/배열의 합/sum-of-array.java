import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = null;
		for (int i = 0; i < 4; i++) {
			st = new StringTokenizer(br.readLine());
			int sum = 0;
			for (int j = 0; j < 4; j++) {
				sum += Integer.parseInt(st.nextToken());
			}
			sb.append(sum).append("\n");
		}
		System.out.println(sb);
	}
}