
public class Rhombus extends GeometricShape{
	private double diagonal_1;
	private double diagonal_2;
	
	public Rhombus() {
		super();
	}
	
	public Rhombus(String color, double diagonal_1, double diagonal_2) {
		super(color);
		this.diagonal_1 = diagonal_1;
		this.diagonal_2 = diagonal_2;
	}
	
	public double getDiagonal_1() {
		return diagonal_1;
	}

	public void setDiagonal_1(double diagonal_1) {
		this.diagonal_1 = diagonal_1;
	} 

	public double getDiagonal_2() {
		return diagonal_2;
	}

	public void setDiagonal_2(double diagonal_2) {
		this.diagonal_2 = diagonal_2;
	}

	@Override	
	double findArea() {		
		return (0.5 * diagonal_1 * diagonal_2);
	}

	@Override
	public String toString() {
		return super.toString() + "Rhombus [diagonal_1=" + diagonal_1 + ", diagonal_2=" + diagonal_2 + "]";
	}
	
}