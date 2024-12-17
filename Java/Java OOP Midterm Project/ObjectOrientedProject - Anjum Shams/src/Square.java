
public class Square extends GeometricShape{
	private double side;

	public Square() {
		super();
	}
	
	public Square(String color, double side) {
		super(color);
		this.side = side;
	}
	
	public double getSide() {
		return side;
	}

	public void setSide(double side) {
		this.side = side;
	}

	@Override
	double findArea() {		
		return (side * side);
	}

	@Override
	public String toString() {
		return super.toString() + "Square [side=" + side + "]";
	}		

}
