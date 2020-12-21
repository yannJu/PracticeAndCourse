import javax.swing.JFrame;

public class CoffeeCansViewer {
	public static void main(String[] args) {
		JFrame frame = new JFrame();
		
		final int FRAME_WIDTH = 150;
		final int FRAME_HEIGIT = 140;
		
		frame.setSize(FRAME_WIDTH, FRAME_HEIGIT);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		CoffeeCansComponent component = new CoffeeCansComponent();
		frame.add(component);
		
		frame.setVisible(true);
	}

}
