print ("Welcome to gpa calculator")
subs=int(input("Enter number of subjects:"))
marks=[]
gpa=[]

for i in range(subs):
    sub_marks=int(input(f"Give marks in paper {i+1} :"))
    marks.append(sub_marks)


    if sub_marks>100 or sub_marks<0:
        print("invalid marks")
    if sub_marks<40:
        gpa.append(0)
    elif sub_marks>=40 and sub_marks<45:
        gpa.append(4)
    elif sub_marks>=45 and sub_marks<50:
        gpa.append(5)
    elif sub_marks>=50 and sub_marks<60:
        gpa.append(6)
    elif sub_marks>=60 and sub_marks<70:
        gpa.append(7)
    elif sub_marks>=70 and sub_marks<75:
        gpa.append(8)
    elif sub_marks>=75 and sub_marks<80:
        gpa.append(9)
    elif sub_marks>=80 :
        gpa.append(10)

total =sum(marks)
avg = total/subs
gpa_=sum(gpa)/subs
print("\n#### Results:")
print(f"total marks are {total}")
print(f"Average marks are {avg}")
print(f"GPA is :{gpa_}")






print("end")
