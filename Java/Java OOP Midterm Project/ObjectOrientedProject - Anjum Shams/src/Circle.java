
public class Circle extends GeometricShape {
	private double radius;	

	public Circle() {
		super();
	}

	public Circle(String color, double radius) {
		super(color);
		this.radius = radius;
	}

	public double getRadius() {
		return radius;
	}

	public void setRadius(double radius) {
		this.radius = radius;
	}

	@Override
	double findArea() {		
		return (3.142 * radius * radius);
	}

	@Override
	public String toString() {
		return super.toString() + "Circle [radius=" + radius + "]";
	}
	
}
