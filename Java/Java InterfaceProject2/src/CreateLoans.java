	/*  The program demonstrates the concepts of Java Abstract, Inheritance, and Interface.
	 * This program asks the user to input the loan information and select the type of loan and displays it. 
	 * Author: Anjum Shams
	 */

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;

	public class CreateLoans extends JFrame {
		private JLabel LBmessage = new JLabel("Please enter the following information: ");
		private JLabel LBlastName = new JLabel("Please enter the last Name:         ");
		private JLabel LBloanNumber = new JLabel("Please enter the loan Number:     ");
		private JLabel LBloanAmount = new JLabel("Please enter the loan Amount:     ");
		private JLabel LBinterestRate = new JLabel("Please enter the Interest Rate:   ");
		private JLabel LBterm = new JLabel("Please enter the term:                  ");
		private JLabel LBprimeRate = new JLabel("Please enter the prime Rate:       ");
		private JTextField txtLastName = new JTextField(12);
		private JTextField txtLoanNumber = new JTextField(12);
		private JTextField txtLoanAmount = new JTextField(12);
		private JTextField txtInterestRate = new JTextField(12);
		private JTextField txtTerm = new JTextField(12);
		private JTextField txtPrimeRate = new JTextField(12);
		private JLabel LBselect = new JLabel("Please select the type of Loan:                   ");
		private JButton jbtPersonalLoan = new JButton("Personal Loan");
		private JButton jbtBusinessLoan = new JButton("Business Loan");


		public CreateLoans () {
		 setLayout(new FlowLayout(FlowLayout.LEFT, 5, 10));
		 add(LBmessage);
		 add(LBlastName);
		 add(txtLastName);
		 add(LBloanNumber);
		 add(txtLoanNumber);
		 add(LBloanAmount);
		 add(txtLoanAmount);
		 add(LBinterestRate);
		 add(txtInterestRate);
		 add(LBterm);
		 add(txtTerm);
		 add(LBprimeRate);
		 add(txtPrimeRate);
		 add(LBselect);
		 add(jbtPersonalLoan);
		 add(jbtBusinessLoan);
		 
		 jbtPersonalLoan.addActionListener (new ActionListener() {
		 public void actionPerformed(ActionEvent e) {			 
	    	  String lastName = txtLastName.getText();	    	  
	    	  String loanNumber = txtLoanNumber.getText();	    	  
	    	  int term = Integer.parseInt(txtTerm.getText());	    	 
	    	  Double interestRate = Double.parseDouble(txtInterestRate.getText());    	 
	    	  Double loanAmount = Double.parseDouble(txtLoanAmount.getText());		    	  
	    	  Double primeRate = Double.parseDouble(txtPrimeRate.getText());			    	 
	    	  PersonalLoan P1 = new PersonalLoan(loanNumber, lastName, loanAmount, interestRate, term, primeRate);
	    	  JOptionPane.showMessageDialog(null, P1.toString());
		 }
		 });
		 
		 jbtBusinessLoan.addActionListener (new ActionListener() {
		 public void actionPerformed(ActionEvent e) {
			 String lastName = txtLastName.getText();	    	  
	    	 String loanNumber = txtLoanNumber.getText();	    	  
	    	 int term = Integer.parseInt(txtTerm.getText());	    	 
	    	 Double interestRate = Double.parseDouble(txtInterestRate.getText());    	 
	    	 Double loanAmount = Double.parseDouble(txtLoanAmount.getText());		    	  
	    	 Double primeRate = Double.parseDouble(txtPrimeRate.getText());
	    	 BuisinessLoan B1 = new BuisinessLoan(loanNumber, lastName, loanAmount, interestRate, term, primeRate);
	    	 JOptionPane.showMessageDialog(null, B1.toString());
		 }
		 });		
		}
		
		/** Main method */
		public static void main(String[] args) {
		 CreateLoans frame = new CreateLoans();
		 frame.setTitle("Create Loans");
		 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		 frame.setSize(370, 450);
		 frame.setVisible(true);
		}			

	}



