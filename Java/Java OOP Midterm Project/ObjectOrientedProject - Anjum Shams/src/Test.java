/*
 * This program demonstrates four principles of object-oriented programming  Abstraction, Polymorphism, 
 * Inheritance, and Encapsulation (APIE). The program uses ArrayList, for loop and switch case to create 
 * and store fifteen different objects and their areas and outputs the results using a for loop and ArrayList
 * of objects. The user gets to choose to display the output to the console, or to save it to a file.
 * 
 * Author: Anjum Shams
 */

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class Test {

	public static void main(String[] args) {
		ArrayList<Object> arrayOfObjects = new ArrayList<>();
		
		for (int i=0; i<15; i++) {
			int r = (int)(Math.random()*3) +1;
			
		    switch (r) {		      
		      case 1:
		    	  Circle C1 = new Circle("blue", 3);
		    	  if (C1 instanceof GeometricShape) {
		    		  arrayOfObjects.add(C1.toString());
			    	  arrayOfObjects.add("Area = " + C1.findArea());		    		  
		    	  } break;
		    	  
		      case 2:
		    	  Square S1 = new  Square("blue", 5.3);
		    	  if (S1 instanceof GeometricShape) {
		    		  arrayOfObjects.add(S1.toString());
			    	  arrayOfObjects.add("Area = " + S1.findArea());
		    	  } break;
		    	  
		      case 3:
		    	  Rhombus R1 = new  Rhombus("blue", 5.0, 7.0);
		    	  if (R1 instanceof GeometricShape) { 
		    		  arrayOfObjects.add(R1.toString());
			    	  arrayOfObjects.add("Area = " + R1.findArea()); 
		    		  } break;
		    } 
		}
		
		Scanner input = new Scanner(System.in);		
		int selection = 0;
		
		 System.out.println("please enter 1 to display the output to the console, and"
			 		+ " 2 to output to a file: ");
		 selection = input.nextInt();
		 
		 if (selection == 1) {
			 for (int i=0; i<arrayOfObjects.size(); i++) {			
				 System.out.println(arrayOfObjects.get(i));				 	    	
		    }			 
		 }
		 
		 else if (selection == 2) {
			 try {
				 System.out.println("please enter a file name to output the results: ");
				 String fileName;
				 fileName = input.next();
					File f = new File("C:\\tmp\\" + fileName);
					PrintWriter pw = new PrintWriter(f);					
				 
				 for (int i=0; i<arrayOfObjects.size(); i++) {
					 pw.println(arrayOfObjects.get(i));					 				 	    	
			    }//for loop
				 
				 input.close();
			      pw.close();
				 
			 } catch (Exception e) {
				 System.out.println("Unable to open file: " + e);
				 System.exit(0);
				 }//for loop			 
		 }//if statement
		 
		 else {
			 System.out.println("invalid data detected. Please enter a correct value.");			 
		 }// else statement			 	

	}//main

}//class
