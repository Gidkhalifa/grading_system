print("hello welcome to student score management system")
student=[]

def Grade(grade):
    g=""
    if grade>=80:
        g="A"
    elif grade >=70:
        g="B"
    elif grade >=60:
        g="C"  

    elif grade>=50:
        g="D"

    else:
        g="F"   
    return g     


out=False

while not out:
    print("1 adding student")
    print("2 view student")
    print("3 remove student")
    print("4 exit")
    print()
    choice=int(input("choice...: "))
    if choice < 1 or choice > 4:
        print("follow the instructions")
    
    else:
        if choice == 1:
           
            list_length=int(input("enter lenth of student list:  "))
            for i in range (1,list_length+1):
                student_name=input("enter name: ")
                grade=int(input("input grade: "))
                student.append([student_name,grade])
        elif choice==2:
             avrage=0
             # display  all students and ther grade
             if len(student)==0:
                 print("cant display empty list")
             for i in student:
                 avrage=avrage+i[1]
                 
                 print(f"NAME: {i[0]}  ->  {i[1]}   GRADE: {Grade(i[1])} ")
             avrage=(avrage)/len(student)
             print(f"average score {avrage}")

             print()
        elif choice==3:
            print("remove student by name")
            Name=input("remove : ")
            for name in student:
                if name[0]==Name:
                    student.remove(name)
        

        else:
            out=True
            print("thanks see you next time")

