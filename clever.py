import clever

clever.set_token("DEMO_TOKEN")

sectionNumber = 0;
studentNumber = 0;

sections = clever.Section.all()
for section in sections:
    sectionNumber+=1
    for student in section.students:
        studentNumber += 1

averageStudentPerSection = studentNumber//sectionNumber
print(averageStudentPerSection)