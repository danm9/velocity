velocity = input("Current Velocity: ")
#print(velocity)
total_team_members = input("Total Team Members: ")
total_days_out_per_sprint = input("Total Days Out: ")
total_days_in_sprint = input("Total Days in Sprint: ")
average_injections = input("Average Injections Per Sprint: ")
total_days_in_sprint_for_team = int(total_team_members) * int(total_days_in_sprint)
#print(total_days_in_sprint_for_team)
velocity_per_person_per_day = int(velocity) / int(total_days_in_sprint_for_team)
#print(velocity_per_person_per_day)
plan_for = int(velocity) - (int(total_days_out_per_sprint) * float(velocity_per_person_per_day)) - (int(average_injections) * 2)
#print(plan_for)
print("Plan For " + str(round(plan_for)))

close_check = input("Are you done?: ")
if close_check == 'yes':
    print("Thanks Boss")
else: 
    print("Tough")
