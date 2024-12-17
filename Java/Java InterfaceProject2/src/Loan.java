
public abstract class Loan implements LoanConstants {	 
	    private String loanNumber;
	    private String lastName;
	    private double loanAmount;
	    protected double interestRate; 
	    private int term;	    
	    
		public Loan() {
			super();
		}

		public Loan(String loanNumber, String lastName, double loanAmount, double interestRate, int term) {
			super();
			this.loanNumber = loanNumber;
			this.lastName = lastName;
			this.loanAmount = loanAmount;
			this.interestRate = interestRate;
			this.term = term;
		}

		public String getLoanNumber() {
			return loanNumber;
		}

		public void setLoanNumber(String loanNumber) {
			this.loanNumber = loanNumber;
		}

		public String getLastName() {
			return lastName;
		}

		public void setLastName(String lastName) {
			this.lastName = lastName;
		}

		public double getLoanAmount() {
			return loanAmount;
		}

		public void setLoanAmount(double loanAmount) {
			this.loanAmount = loanAmount;
		}

		public double getInterestRate() {
			return interestRate;
		}

		public void setInterestRate(double interestRate) {
			this.interestRate = interestRate;
		}

		public int getTerm() {
			return term;
		}

		public void setTerm(int term) {
			this.term = term;
		}

     public void checkLoanAmountAndSetTerm(double loanAmount) {
            if (loanAmount > MAX_LOAN_AMOUNT) {
                System.out.println("This loan amount exceeds the maximum loan amount of 500000");
            }
            else {            
            	setLoanAmount(loanAmount);
            } 
            
            if  (term<1 || term>5) {
            	setTerm(1);   
    }
     }
		

		@Override
		public String toString() {
			return "Loan [loanNumber=" + loanNumber + ", lastName=" + lastName + ", loanAmount=" + loanAmount
					+ ", interestRate=" + interestRate + ", term=" + term + "]";
		}
		
		
	    
	    
	    
	    
	}
	    


