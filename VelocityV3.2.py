#v3 -> v3.2 taking out the total days in sprint, leaving them set at 10

#method to recalc based on different team size or to keep the same team size
def velocity_calc(): 
    answer = input("Do you have a different team size?(Y/N): ")
    if answer.lower() == 'y':
        #Previous Sprint Info
        current_velocity = input("Current Velocity: ")
        old_team_count = input("Team Members in Previous Sprint: ")
        velocity_calc = float(current_velocity) / (float(old_team_count) * 10)
        new_team_members = input("Total Team Members in New Sprint: ")
        new_velocity = float(velocity_calc) * float(new_team_members) * 10
        print("Use " + str(round(new_velocity)) + " for your Velocity")
        
        #new sprint info
        velocity = input("Sprint Velocity: ")
        total_team_members = input("Total Team Members in New Sprint: ")
        total_days_out = input("Total Days Out: ")
        average_injections = input("Average Injections Per Sprint: ")
        deploys = input("How Many Deploys for This Sprint: ")
        rollover_points = input("How Many Rollover Points this Sprint: ")
        
        #Calculations for new velocity, Deploys are set at 2 hours
        deploy_time = float(deploys) * 2
        total_hours_out_per_sprint = float(total_days_out) * 6 + float(deploy_time)
        total_days_out_per_sprint = float(total_hours_out_per_sprint) / 6
        velocity_per_person_per_day = float(velocity) / (10 * float(total_team_members))
        plan_for = float(velocity) - (float(total_days_out_per_sprint) * float(velocity_per_person_per_day)) - (float(average_injections) * 2) - float(rollover_points)
        print("Plan For " + str(round(plan_for)))
    else:
        #same amount of team members
        velocity = input("Sprint Velocity: ")
        total_team_members = input("Total Team Members in New Sprint: ")
        total_days_out = input("Total Days Out: ")
        average_injections = input("Average Injections Per Sprint: ")
        deploys = input("How Many Deploys for This Sprint: ")
        rollover_points = input("How Many Rollover Points this Sprint: ")
        
        #Calculations for new velocity
        deploy_time = int(deploys) * 2
        total_hours_out_per_sprint = float(total_days_out) * 6 + float(deploy_time)
        total_days_out_per_sprint = float(total_hours_out_per_sprint) / 6
        velocity_per_person_per_day = float(velocity) / (10 * float(total_team_members))
        plan_for = float(velocity) - (float(total_days_out_per_sprint) * float(velocity_per_person_per_day)) - (float(average_injections) * 2) - float(rollover_points)
        print("Plan For " + str(round(plan_for)))

velocity_calc()
#to keep the .py open longer
done = input("")
