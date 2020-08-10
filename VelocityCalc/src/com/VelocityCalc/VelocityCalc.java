package com.VelocityCalc;
import java.util.Scanner;

public class VelocityCalc {
    public static void main(String[] args) {
        /** Old Sprint Info */
        String teamDifference;
        double currentVelocity;
        double oldTeamCount;
        double calcVelocity;
        double newTeamCount;
        double newVelocity;

        /** New Sprint Info */
        double velocity;
        double totalTeamMembers;
        double totalDaysOut;
        double averageInjections;
        double additionalHoursSubtracted;
        double rolloverPoints;

        /** Used for calculations */
        double totalHoursOutPerSprint;
        double totalDaysOutPerSprint;
        double velocityPerPersonPerDay;
        double planFor;

        Scanner input = new Scanner(System.in);

        /** Previous Sprint Info
         * The if statement will run if True to find new Velocity */

        System.out.print("Do you have a different team size?(Y/N): ");
        teamDifference = input.next();

        if (teamDifference.equalsIgnoreCase("Y")) {
            System.out.print("Current Velocity: ");
            currentVelocity = input.nextDouble();

            System.out.print("Team Members in Previous Sprint: ");
            oldTeamCount = input.nextDouble();
            calcVelocity = currentVelocity/oldTeamCount;

            System.out.print("Total Team Members in New Sprint: ");
            newTeamCount = input.nextDouble();
            newVelocity = calcVelocity * newTeamCount;

            System.out.println("Use " + Math.round(newVelocity) + " for your velocity");

        }

        System.out.print("Sprint Velocity: ");
        velocity = input.nextDouble();

        System.out.print("Total Team Members in New Sprint: ");
        totalTeamMembers = input.nextDouble();

        System.out.print("Total Days Out: ");
        totalDaysOut = input.nextDouble();

        System.out.print("Average Injections Per Sprint: ");
        averageInjections = input.nextDouble();

        System.out.print("How Many Additional Hours Subtracted for This Sprint: ");
        additionalHoursSubtracted = input.nextDouble();

        System.out.print("How Many Rollover Points this Sprint: ");
        rolloverPoints = input.nextDouble();

        totalHoursOutPerSprint = totalDaysOut * 6 + additionalHoursSubtracted;
        totalDaysOutPerSprint = totalHoursOutPerSprint / 6;
        velocityPerPersonPerDay = velocity / (10 * totalTeamMembers);
        planFor = velocity - (totalDaysOutPerSprint * velocityPerPersonPerDay) -
                (averageInjections * 2) - rolloverPoints;
        System.out.println("Plan for " + Math.round(planFor) + " points" );
    }
}

