import tkinter as tk

fields = ('Velocity', 'Total Team Members', 'Sprint Length', 'Total Days Out', 'Average Injections', 
'Average Injection Effort', 'Additional Hours Subtracted', 'Rollover Points', )

def sprint(x):
    if x == 1:
        y = 5
    elif x == 2:
        y = 10
    elif x == 3:
        y = 15
    else:
        y = 20
    return y

def velocity_calc(entries):
    hours_per_day = 6
    velocity = float(entries['Velocity'].get())
    total_team_members = float(entries['Total Team Members'].get())
    sprint_length = float(entries['Sprint Length'].get())
    total_days_out = float(entries['Total Days Out'].get())
    average_injections = float(entries['Average Injections'].get())
    average_injection_effort = float(entries['Average Injection Effort'].get())
    additional_hours = float(entries['Additional Hours Subtracted'].get())
    rollover_points = float(entries['Rollover Points'].get())

    sprint_day_count = sprint(sprint_length)
    sprint_hours = float(sprint_day_count) * float(hours_per_day) * float(total_team_members)
    hours_per_point = float(sprint_hours) / float(velocity)
    injection_points = float(average_injections) * float(average_injection_effort)

    total_hours_out_per_sprint = float(total_days_out) * float(hours_per_day) + float(additional_hours)
    total_days_out_per_sprint = float(total_hours_out_per_sprint) / float(hours_per_day)
    velocity_per_person_per_day = float(velocity) / (float(sprint_day_count) * float(total_team_members))
    plan_for = float(velocity) - (float(total_days_out_per_sprint) * float(velocity_per_person_per_day)) - float(injection_points) - float(rollover_points)         
    res.configure(text = (f"Plan For {round(plan_for)}, Total for the Sprint Would Be {round(plan_for) + round(injection_points) + round(rollover_points)}"))
    # print(f"""
    # Numbers You Chose For Your Sprint:
    #     Velocity: {velocity}
    #     Team Size: {total_team_members}
    #     Sprint Length: {sprint_length} Weeks
    #     Total Days Out: {total_days_out}
    #     Injections: {average_injections}
    #     Rollover Points: {rollover_points}

    # Calculations for Your Sprint:
    #     The Hours-Per-Point Will Be: {hours_per_point}
    #     Total Points Used for Injections: {injection_points}
    #     Total Hours Out for the Team: {total_hours_out_per_sprint}
    #     If Using a 6 Hour Day of Total Development, Total Days Out: {total_days_out_per_sprint}
    #     Velocity-Per-Person for This Sprint: {velocity_per_person_per_day}
        
    # Plan For {round(plan_for)}, Total for the Sprint Would Be {round(plan_for) + round(injection_points) + round(rollover_points)}
    #         """)
def makeform(w, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(w)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[field] = ent
    return entries

w = tk.Tk()
w.geometry('400x325')
w.title("Velocity Calculator")
ents = makeform(w, fields)
b1 = tk.Button(w, text='Get Summary', command=(lambda e=ents: velocity_calc(e)))
b1.pack(side=tk.LEFT, padx=5, pady=5)
b2 = tk.Button(w, text='Quit', command=w.quit)
b2.pack(side=tk.LEFT, padx=5, pady=5)
res=tk.Label(w)
res.pack()
w.mainloop()