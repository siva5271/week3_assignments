writtenTest=int(input("Enter the written test score"))
labExam=int(input("Enter the lab exams score"))
assignments=int(input("Enter the assignments score"))

grade=((writtenTest*7)+(labExam*2)+(assignments))/10
print("Grade:",grade)