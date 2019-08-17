ximport csv

with open('C:\\Users\\user\\example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    work_item_type = []
    tags = []
    effort = []
    statuses = []
    for row in readCSV:
        item = row[0]
        tag = row[1]
        e = row[2]
        status = row[3]

        work_item_type.append(item)
        tags.append(tag)
        effort.append(e)
        statuses.append(status)
    
    bugs = int(work_item_type.count('Bug'))
    pbis = int(work_item_type.count('Product Backlog Item'))
    bugcrowd_items = int(work_item_type.count('BugCrowd Items'))
    total = bugs + pbis + bugcrowd_items
    injections = int(tags.count('Injection'))
    
    #velocity = int(effort.count)

    print(
    'Bugs: ' + str(bugs) + "\n"
    'PBIs: ' + str(pbis) + "\n"
    'BugCrowd Items: ' + str(bugcrowd_items) + "\n"
    'Total PBIs/Bugs Completed: ' + str(total) + "\n"
    'Injections: ' + str(injections) + "\n"
    )

