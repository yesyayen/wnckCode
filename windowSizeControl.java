import java.awt.Frame;
import java.awt.GraphicsConfiguration;
import java.awt.GraphicsEnvironment;
import java.awt.Insets;
import java.awt.LayoutManager;
import java.awt.Toolkit;

import javax.swing.JFrame;
import javax.swing.JLabel;


public class samp 
{
	static GraphicsConfiguration gc = new Frame().getGraphicsConfiguration();
	public static void main(String args[]) throws InterruptedException
	{
		System.out.println(Toolkit.getDefaultToolkit().getScreenSize());
		
		int height=Toolkit.getDefaultToolkit().getScreenSize().height;
		int width=Toolkit.getDefaultToolkit().getScreenSize().width;
		
		int UseWidth= GraphicsEnvironment.getLocalGraphicsEnvironment().getMaximumWindowBounds().width;
		int UseHeight=GraphicsEnvironment.getLocalGraphicsEnvironment().getMaximumWindowBounds().height;

		int midWidth= UseWidth/2;
		int midHeight=UseHeight/2;
		
		int currentHeight;	
		int currentWidth;
		
		JFrame frame = new JFrame("Test");
		frame.setVisible(true);
		
		JLabel label=new JLabel();
		
		frame.add(label);
	//	Insets ins= Toolkit.getDefaultToolkit().getScreenInsets(gc);
	//	System.out.println(ins);
		// frame.setSize(500,200);
		
		frame.setBounds(0,0,UseWidth/2,UseHeight/2);
		currentHeight=frame.getSize().height;
		currentWidth=frame.getSize().width;
		
		label.setText("Quad 1");
		Thread.sleep(1000);
		frame.setBounds(UseWidth/2,0,UseWidth/2,UseHeight/2);
		label.setText("Quad 2");
		Thread.sleep(1000);
		frame.setBounds(0,UseHeight/2,UseWidth/2,UseHeight/2);
		label.setText("Quad 3");
		Thread.sleep(1000);
		frame.setBounds(UseWidth/2,UseHeight/2,UseWidth/2,UseHeight/2);
		label.setText("Quad 4");
		Thread.sleep(1000);
		
		frame.setBounds(midWidth-currentWidth/2,midHeight-currentHeight/2,currentWidth,currentHeight);
		label.setText("Center");
		Thread.sleep(1000);
		
		frame.setBounds(0,0,midWidth,UseHeight);
		label.setText("Left");
		Thread.sleep(1000);
		
		frame.setBounds(midWidth,0,midWidth,UseHeight);
		label.setText("Right");
		Thread.sleep(1000);
		
		frame.setBounds(0,0,UseWidth,midHeight);
		label.setText("Top");
		Thread.sleep(1000);
		
		currentHeight=frame.getSize().height;
		currentWidth=frame.getSize().width;
		frame.setBounds(midWidth-currentWidth/2,midHeight-currentHeight/2,currentWidth,currentHeight);
		label.setText("Center");
		Thread.sleep(1000);
		
		frame.setBounds(0,midHeight,UseWidth,midHeight);
		label.setText("Bottom");
		Thread.sleep(1000);
		
		
		//frame.setBounds(arg0, arg1, arg2, arg3);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
