import javax.swing.JComponent;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Ellipse2D; 

public class CoffeeCansComponent extends JComponent{

	public void paintComponent(Graphics g){
		Graphics2D g2 = (Graphics2D) g;
		for (int i = 1; i <= 6; i ++) {
			for (int j = 1; j <= 4; j ++) {
				Ellipse2D.Double can = new Ellipse2D.Double(10*(2*i - 1), (2*j-1)* 10, 20, 20);
				g2.draw(can);
			}
		}
	}
}

