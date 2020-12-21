package academyforjava;
import java.io.*;
import java.util.Scanner;

class ArrayQ{
	private int []space;
	private int sl;
	private int start ;
	private int end ;
	private int count;
	void ArrayQ() {
		start = 0;
		end = 0;
		count = 0;
	}
	void makespace() throws IOException{
		BufferedReader spacelength = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("How Long?>>");
		sl = Integer.parseInt(spacelength.readLine());
		space = new int[sl];
	}//�迭 ���� �����
	void Enqueue(int a) {
		if (CheckOverflow()) {
			if (end == sl) {
				end = 0;
			}
			space[end++] = a;
			count++;
		}
		else {
			System.out.println("Over Flow");
		}//overflow�϶�
	}//Enqueue�϶�
	void Dequeue() {
		if (CheckUnderflow()) {
			if (start+1 > sl) {
				start = 0;
			}
			System.out.println("Dequeue Num is" + space[start++]);
			count--;
		}
		else {
			System.out.println("Under Flow");
		}
	}
	boolean CheckOverflow() {
		if (count<sl) {
			return true;
		}
		else {
			return false;
		}
	}//overflow Ȯ��
	boolean CheckUnderflow() {
		if (count <= 0) {
			return false;
		}
		else {
			return true;
		}
	}//underflow Ȯ��
}
public class JavaQueue {

	public static void main(String[] args) throws IOException {
		BufferedReader sore = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Choose 1 or 2 (1.Start 2.End) >>");
		Integer se = Integer.parseInt(sore.readLine());
		ArrayQ aq = new ArrayQ();
		aq.makespace(); //�迭 ����
		while (se == 1) {
			Scanner eordorq = new Scanner(System.in);
			System.out.println("Input \"Enqueue\" or \"Dequeue\" or \"Quick\"");
			String edq = eordorq.nextLine(); //enqueue dequeue quick ����
			if (edq.equals("Enqueue")) {
				BufferedReader enqueuenum = new BufferedReader(new InputStreamReader(System.in));
				System.out.println("WhatNumber?>>");
				Integer en = Integer.parseInt(enqueuenum.readLine());
				aq.Enqueue(en);
			}//Enqueue �϶�
			else if (edq.equals("Dequeue")) {
				aq.Dequeue();
			}//Dequeue�϶�
			else if (edq.equals("Quick")) {
				System.out.println("End:)");
				se = 2;
			}//Quick�϶�
			else {
				System.out.println("Only Input \"Enqueue\" or \"Dequeue\" or \"Quick\", Please Input Again.");
			}//�ٸ����� �Է� ������
		}//Queue�� ���ư��� ���� ����(Start�϶�)
	}//main
	
}
