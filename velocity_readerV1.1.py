#v1.1

import csv
import re

with open('C:\\Users\\dminahan\\python\\velocity\\CHANGE.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    ids = []
    states = []
    work_item_type = []
    tags = []
    effort = []
    statuses = []
    
    for row in readCSV:
        id = row[0]
        state = [1]
        item = row[2]
        tag = row[3]
        e = row[4]
        status = row[5]

        #putting each item into a list  
        work_item_type.append(item)
        tags.append(tag)
        effort.append(e)
        statuses.append(status)

    #counting the Bugs/PBIs/BugCrowd Items and effort
    bugs = int(work_item_type.count('Bug'))
    pbis = int(work_item_type.count('Product Backlog Item'))
    bugcrowd_items = int(work_item_type.count('BugCrowd Items'))
    total = bugs + pbis + bugcrowd_items

    #remove null values in list and get total effort count    
    for r in effort:
        if r == '':
            effort.remove('')
    
    effort_count = effort[1:]

    #Converting effort_count from a list to INTs
    for i in range(0, len(effort_count)):
        effort_count[i] = float(effort_count[i])


    #stripping the injections out and counting them    
    injections = 0
    injection_value_list = []
    for tag in tags:
        tokens = tag.split(';')
        for token in tokens:
            if token.strip() == 'Injection':
                injections+=1

    #Prints
    print(
    'Bugs: ' + str(bugs) + "\n"
    'PBIs: ' + str(pbis) + "\n"
    'BugCrowd Items: ' + str(bugcrowd_items) + "\n"
    'Total PBIs/Bugs Completed: ' + str(total) + "\n"
    'Injections: ' + str(injections) + "\n"
    'Velocity: ' + str(sum(effort_count))
    )

    
