velocity = input("Current Velocity: ")
#print(velocity)
total_team_members = input("Total Team Members: ")
total_days_out = input("Total Days Out: ")
total_days_in_sprint = input("Total Days in Sprint: ")
average_injections = input("Average Injections Per Sprint: ")
deploys = input("How Many Deploys for This Sprint: ")
deploy_time = int(deploys) * 2
total_hours_out_per_sprint = int(total_days_out) * 6 + int(deploy_time)
total_days_out_per_sprint = int(total_hours_out_per_sprint) / 6
velocity_per_person_per_day = int(velocity) / (int(total_days_in_sprint) * int(total_team_members))
#print(velocity_per_person_per_day)
plan_for = int(velocity) - (int(total_days_out_per_sprint) * float(velocity_per_person_per_day)) - (int(average_injections) * 2)
print("Plan For " + str(round(plan_for)))

close_check = input("Are you done?: ")
if close_check == 'yes':
    print("Thanks Boss")
else: 
    print("Tough")
