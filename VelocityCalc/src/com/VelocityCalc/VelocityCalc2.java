/** need to update injections...see python script for all the changes
 */


package com.VelocityCalc;
import java.util.InputMismatchException;
import java.util.Scanner;

public class VelocityCalc2 {
    public static void main(String[] args) {
        boolean runVelocityCalc = true;

        /** Old Sprint Info */
        String teamDifference;
        double currentVelocity = 0.0;
        double oldTeamCount = 0.0;
        double calcVelocity = 0.0;
        double newTeamCount = 0.0;
        double newVelocity = 0.0;

        /** New Sprint Info */
        double velocity = 0.0;
        double totalTeamMembers = 0.0;
        double totalDaysOut = 0.0;
        double averageInjections = 0.0;
        double additionalHoursSubtracted = 0.0;
        double rolloverPoints = 0.0;

        /** Used for calculations */
        double totalHoursOutPerSprint = 0.0;
        double totalDaysOutPerSprint = 0.0;
        double velocityPerPersonPerDay = 0.0;
        double planFor = 0.0;

        Scanner input = new Scanner(System.in);

        /** Previous Sprint Info
         * The if statement will run if True to find new Velocity */

        while (runVelocityCalc) {
            System.out.print("What do you want to Calc?(V=Velocity, N=New Team Velocity, Q=Quit): ");
            teamDifference = input.next();
            if (teamDifference.equalsIgnoreCase("Q")) {//quit
                runVelocityCalc = false;
                System.out.println("\nProgram Ended");
            }
            else if (teamDifference.equalsIgnoreCase("N")) {
                System.out.print("Current Velocity: ");
                try {
                    currentVelocity = input.nextDouble();
                }
                catch (InputMismatchException e) {
                    System.err.println(e + ": You entered an invalid number!" +
                            "\nIt must be a numeric value.");
                    System.exit(1);
                }

                System.out.print("Team Members in Previous Sprint: ");
                try{
                    oldTeamCount = input.nextDouble();
                    calcVelocity = currentVelocity / oldTeamCount;
                }
                catch (InputMismatchException e) {
                    System.err.println(e + ": You entered an invalid number!" +
                            "\nIt must be a numeric value.");
                    System.exit(1);
                }

                System.out.print("Total Team Members in New Sprint: ");
                try {
                    newTeamCount = input.nextDouble();
                    newVelocity = calcVelocity * newTeamCount;
                }
                catch (InputMismatchException e) {
                    System.err.println(e + ": You entered an invalid number!" +
                            "\nIt must be a numeric value.");
                    System.exit(1);
                }

                System.out.println("Use " + Math.round(newVelocity) + " for your velocity");
            }
            else if (teamDifference.equalsIgnoreCase("V")){
                System.out.print("Sprint Velocity: ");
                try {
                    velocity = input.nextDouble();
                }
                catch (InputMismatchException e) {
                    System.err.println(e + ": You entered an invalid number!" +
                            "\nIt must be a numeric value.");
                    System.exit(1);
                }

                System.out.print("Total Team Members in New Sprint: ");
                try {
                    totalTeamMembers = input.nextDouble();
                }
                catch (InputMismatchException e) {
                    System.err.println(e + ": You entered an invalid number!" +
                            "\nIt must be a numeric value.");
                    System.exit(1);
                }
                System.out.print("Total Days Out: ");
                try {
                    totalDaysOut = input.nextDouble();
                }
                catch (InputMismatchException e) {
                    System.err.println(e + ": You entered an invalid number!" +
                            "\nIt must be a numeric value.");
                    System.exit(1);
                }

                System.out.print("Average Injections Per Sprint: ");
                try {
                    averageInjections = input.nextDouble();
                }
                catch (InputMismatchException e) {
                    System.err.println(e + ": You entered an invalid number!" +
                            "\nIt must be a numeric value.");
                    System.exit(1);
                }

                System.out.print("How Many Additional Hours Subtracted for This Sprint: ");
                try {
                    additionalHoursSubtracted = input.nextDouble();
                }
                catch (InputMismatchException e) {
                    System.err.println(e + ": You entered an invalid number!" +
                            "\nIt must be a numeric value.");
                    System.exit(1);
                }

                System.out.print("How Many Rollover Points this Sprint: ");
                try {
                    rolloverPoints = input.nextDouble();
                    totalHoursOutPerSprint = totalDaysOut * 6 + additionalHoursSubtracted;
                    totalDaysOutPerSprint = totalHoursOutPerSprint / 6;
                    velocityPerPersonPerDay = velocity / (10 * totalTeamMembers);
                    planFor = velocity - (totalDaysOutPerSprint * velocityPerPersonPerDay) -
                            (averageInjections * 2) - rolloverPoints;
                    System.out.println("Plan for " + Math.round(planFor) + " points");
                }
                catch (InputMismatchException e) {
                    System.err.println(e + ": You entered an invalid number!" +
                            "\nIt must be a numeric value.");
                    System.exit(1);
                }
            }
            else {
                System.out.println("That's not a V, N, or Q");
                }
        }
    }
}


