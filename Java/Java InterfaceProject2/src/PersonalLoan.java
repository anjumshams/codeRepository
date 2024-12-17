
public class PersonalLoan extends Loan implements LoanConstants {
	private double primeRate;


	public PersonalLoan() {
		super();	
	}
	
	public PersonalLoan(String loanNumber, String lastName, double loanAmount, double interestRate, int term, double primeRate) {
		super(loanNumber, lastName, loanAmount, interestRate, term);
		super.interestRate = 0.02 / (primeRate / 100);		
	}
	
	public double getPrimeRate() {
		return primeRate;
	}

	public void setPrimeRate(double primeRate) {
		this.primeRate = primeRate;
	}	
	
	@Override
	public String toString() {
		return super.toString() + "PersonalLoan [primeRate=" + primeRate + "]";
	}
		
}
