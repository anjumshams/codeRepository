
public class BuisinessLoan extends Loan implements LoanConstants {
	private double primeRate;	

	public BuisinessLoan() {
		super();
		
	}

	public BuisinessLoan(String loanNumber, String lastName, double loanAmount, double interestRate, int term, double primeRate) {
		super(loanNumber, lastName, loanAmount, interestRate, term);
		super.interestRate = 0.01 / (primeRate / 100);		
	}
	
	

	public double getPrimeRate() {
		return primeRate;
	}

	public void setPrimeRate(double primeRate) {
		this.primeRate = primeRate;
	}

	@Override
	public String toString() {
		return super.toString() + "BuisinessLoan [primeRate=" + primeRate + "]";
	}	
	
}
	


	
	
	


	
	
	
	
	
	


