
public abstract class GeometricShape {
	private String color;

	public GeometricShape() {
		super();
	}

	public GeometricShape(String color) {
		super();
		this.color = color;
	}

	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}
	
	abstract double  findArea();

	@Override
	public String toString() {
		return "GeometricShape [color=" + color + "]";
	}	

}
