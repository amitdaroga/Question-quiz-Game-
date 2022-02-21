import random as R
def show_score(Email):
    f_score=open('score','r')
    student_score=f_score.readlines()
    for i in student_score:
        i=i.split()
        if Email in i:
            print("\n")
            print("*"*20)
            print("your name :",i[0])
            print("your last score :",i[1])
            print("*"*20)
def score_addtion(user_name,score):
    f_score=open('score','r')
    data=list(f_score.read().split('\n'))
    f_score.close()
    f_score=open('score','w')
    for i in data:
        uname = i.split()
        if user_name in uname:
            uname.pop(1)
            uname.append(str(score))
            for i in uname:
                f_score.write(str(i)+'\t')
            f_score.write('\n')
        else:
            f_score.write(i+'\n')
    f_score.close()

def student_registration(username,Email,password):
    file=open("student_details",'a')
    file.writelines(username+" "+Email+" "+password+"\n")
    file.close()
    file_score_append=open('score','a')
    score=0
    file_score_append.write(username+"\t"+str(score)+'\n')
    file_score_append.close()
    return "your is completed registration" 

def student_login(Email,password):
    file=open("student_details",'r')
    for i in file:
        read=i.split()
        if Email in read and password in read:
            if Email in read[0] and password in read[-1]:
                file.close()
                return True
        


def teacher_registration(username,Email,password):
    file=open("teacher_details",'a')
    file.writelines(username+" "+Email+" "+password+"\n")
    file.close
    return "your is completed registration" 
def teacher_login(Email,password):
    file=open("teacher_details",'r')
    for i in file:
        read=i.split()
        if Email in read and password in read:
            file.close
            return True
        else:
            file.close
            return False
def seequestion():
    dic={}
    read1=open("question_list",'r')
    for i in read1:
        read=i.split()
        q=read[0]
        read.pop(0)
        q=q.replace("_"," ")
        dic[q]=read
    read1.close
    return dic
while True:
    #asking user you are student or teacher 
    choice=input("1:teacher\n2:student\n3:exit\nplease enter your choice :: ")
    if choice=='1':
        #teacher page to choice Registration  ro login
        while True:
            teacher_choice=input("1:Login\n2:Registration\n3:exit\nplease enter your choice :: ")
            if teacher_choice=='1':
                #Login page
                Email=input("Enter username :")
                password=input("Enter password :")
                Email=Email.replace(" ","_")
                if teacher_login(Email,password)==True:
                    while True:
                        choice1=input("1:add question\n2:see all question\n3:logout\nplease Enter your choice :: ")
                        if choice1=='1':
                             question=input("Enter question :: ")
                             question=question.replace(" ","_")
                             print(question)
                             a='a.'
                             b='b.'
                             c='c.'
                             d='d.'
                             a+=input("Enter A option value :: ")
                             b+=input("Enter B option value :: ")
                             c+=input("enter C option value :: ")
                             d+=input("Enter D option value :: ")
                             ans=input("enter right option for your question :: ")
                             file=open("question_list","a")
                             file.writelines(question+" "+a+" "+" "+b+" "+c+" "+d+" "+ans+"\n")
                             file.close
                        elif choice1=='2':
                            count=1
                            calling=seequestion()
                            for i in calling:
                                print("Q",count,i)
                                read=calling[i]
                                print(read[0],"\t",read[1],"\n",read[2],"\t",read[3],end="")
                                print("right Ans-->",read[4])    
                                count+=1
                        elif choice1=='3':
                            print("curent account is logout ")
                            break
                        else:
                            print("invalid input")
                else:
                    print("Please check Email id or password wrong")

            elif teacher_choice=='2':
                #Registration page
                username=input("Enter your name :")
                Email=input("Enter Email Id :")
                password=input("Enter password :")
                username=username.replace(" ","_")
                #calling teacher_registration function
                teacher=teacher_registration(username,Email,password)
                print(teacher+"\n\n\n")
            elif teacher_choice=='3':
                #exit for page
                break
            else:
                print("invalid input ")
    elif choice=='2':
        student_choice=input("1:Login\n2:Registration\n3:exit\nplease enter your choice :: ")
        if student_choice=='1':
             #Login page
             Email=input("Enter username :")
             password=input("Enter password :")
             Email=Email.replace(" ","_")
             if student_login(Email,password)==True:
                score = 0
                print("welcome :",Email)
                while True:
                    student_option=input("1:question Quiz\n2:your score\n3:logout\nplease enter your choice->")
                    if student_option=='1':
                        li=[]
                        calling=seequestion()
                        for i in calling.keys():
                            li.append(i)
                        for i in range(1,6):
                            q=R.choice(li)
                            print(i,".",q)
                            li2=calling[q]
                            li.remove(q)
                            print(li2[0]+"\t"+li2[1]+"\n"+li2[2]+"\t"+li2[3],end="\t")
                            option_choice=input("-->")
                            if option_choice==li2[4]:
                                print("ans right")
                                score = score+10
                            else:
                                print("wrong ans")
                            print("Your score is :: ",score)
                        score_addtion(Email,score)
                        print("*"*60)
                        
                        

                    elif student_option=='2':
                        show_score(Email)
                        
                    elif student_option=='3':
                        print("current account is logout ")
                        break
                    else:
                        print("invalid input ")
             else:
                 print("Please check your username or password is wrong ")

        elif student_choice=='2':
            #Registration page
            username=input("Enter your name :")
            Email=input("Enter Email Id :")
            password=input("Enter password :")
            username=username.replace(" ","_")
            teacher=student_registration(username,Email,password)
            print(teacher+"\n\n\n")
    elif choice=='3':
        print("3")
        break
    else:
        print("invalid input ")