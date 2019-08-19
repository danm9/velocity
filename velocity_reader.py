import csv

with open('C:\\Users\\dminahan\\python\\velocity\\Consumer_velocity.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    work_item_type = []
    tags = []
    effort = []
    statuses = []
    
    for row in readCSV:
        item = row[2]
        tag = row[3]
        e = row[4]
        status = row[5]

#putting each item into a list
        work_item_type.append(item)
        tags.append(tag)
        effort.append(e)
        statuses.append(status)
    
#counting the Bugs/PBIs/BugCrowd Items
    bugs = int(work_item_type.count('Bug'))
    pbis = int(work_item_type.count('Product Backlog Item'))
    bugcrowd_items = int(work_item_type.count('BugCrowd Items'))
    total = bugs + pbis + bugcrowd_items
    injections = int(tags.count('Injection'))
    effort_count = effort[1:]

#Converting the list from STR to INT
    for i in range(0, len(effort_count)):
        effort_count[i] = int(effort_count[i])

#Prints
    print(
    'Bugs: ' + str(bugs) + "\n"
    'PBIs: ' + str(pbis) + "\n"
    'BugCrowd Items: ' + str(bugcrowd_items) + "\n"
    'Total PBIs/Bugs Completed: ' + str(total) + "\n"
    'Injections: ' + str(injections) + "\n"
    'Velocity: ' + str(sum(effort_count))
    )


