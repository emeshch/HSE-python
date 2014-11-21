with open("projects.csv") as file:
    projects = {}
    elems = []
    for line in file:
        #print(line)
        elems = line.rstrip().split(';')
        pr_name = elems.pop(0)
        projects[pr_name] = elems
        #projects.update({pr_name:elems})
        #print("PROJECTS", projects)
#print(projects)

with open("students.csv") as file:
    students = {}
    rr = ""
    for line in file:
        #print("line", line)
        line = line.rstrip()
        info = line.split(';')
        #print("info", info)
        stname = info.pop(0)
        if stname not in students:
            students[stname] = []
            students[stname].append(info)
            #print(students[stname])
            for pr in projects:
                if stname in projects[pr]:
                    students[stname].append(pr)
                    line = line + ";" + pr + "\n"
            rr = rr + line           
print(rr)

file = open("stdent-projects.csv", "r+")                   
file.write(rr)
print(file.read())
file.close

