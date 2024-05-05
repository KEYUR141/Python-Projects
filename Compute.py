def average_marks(marks):
    total = 0
    subjects = len(marks)
    for i in marks:
        total+=i
    av_marks = total//subjects
    return av_marks

def compute_grade(av_marks):
    if(av_marks>=90):
        grade='A'
    elif(av_marks>=70):
        grade='B'
    elif(av_marks>=50):
        grade='C'
    else:
        grade='Fail'
    return grade

#Main Function
#Student info
name = input("Enter the student Name:")
dept = input("Enter the your department:")
sem  = input("Enter the semester:")

#Input of the data
s = int(input("Enter the total number of subjects:"))
marks=[]
subjects=[]

for i in range(s):
    sub=input(f'Enter the name of the subject {i+1}:')
    subjects.append(sub)

    marks1=int(input(f'Enter the marks for the {sub}:'))
    marks.append(marks1)

#Marksheet
#Marksheet: student info
print(f'Name:{name}, Department:{dept}, Sem:{sem}\n')

#Marksheet: student's all subjects marks
for i in  range(s):
    print(f'{subjects[i]}:{marks[i]}')

#Marksheet: computed average marks and grades
average = average_marks(marks)
print("\nAverage marks:",average)

compute = compute_grade(average)
print("Grade:",compute)
    