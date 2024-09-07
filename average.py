ct=1
li=[]
decision=str(input("k, so you wanna get da average grade, highest grade or what?"))
if "average" in decision.lower():
    student_numb=int(input("how many students?, "))
    for i in range(0,student_numb):
        grade=int(input(f"what da grade of student {ct}? "))
        ct+=1
        li.append(grade)
    sum_of_hight=(sum(li))
    print(sum_of_hight/student_numb)

elif "highest" in decision.lower():
    student_numb=int(input("how many students?, "))
    for i in range(0,student_numb):
        grade=int(input(f"what da grade of student {ct}? "))
        if grade>
        ct+=1
        li.append(grade)
    li.sort()
    print(li[-1])
