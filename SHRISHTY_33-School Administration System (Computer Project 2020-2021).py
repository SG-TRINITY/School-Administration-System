#COMPUTER PROJECT TOPIC: SCHOOL ADMINISTRATION SYSTEM
import os
import pickle
import random
import sys

#(1)a)Student admission
def stu_add():
  name=input("Enter the name of the new student:")
  contact=int(input("Enter your contact number:"))
  marks=float(input("Enter the  10th percentile of the new student:"))
  idn=random.randint(1,100000)
  print("Your ID number is:",idn)
  groups(marks)
  print()
  group=input("Please input the letter of your group")
  group=group.upper()
  rec={'IDNO':idn, 'NAME':name, 'MARKS':marks, 'GROUP':group, 'CONTACTS':contact}
  f=open("StudentReg.dat","ab")
  pickle.dump(rec,f)
  print("Records added successfully")
  f.close()
  print()


#(1)b)Eligibilty for groups
def groups(x):
  while True:
    print("The groups offered are:\n1)Science with Mathematics and Computer Science-GROUP A\n2)Science with Mathematics and Engineering Graphics-GROUP B\n3)Science with Biology and Psychology-GROUP C\n4)Commerce with Mathematics and Economics-GROUP D\n5)Commerce with Informatics Practices and Economics-GROUP E\n6)Commerce with Marketing and Information Technology-GROUP F\n7)Humanities with Fine Arts-GROUP G\n8)Humanities without Fine Arts-GROUP H")
    print()
    grp_op=int(input("Please enter your group option to check your eligiblity:"))
    if grp_op==1:
        if x>=80:
            print("Eligible for Science with Mathematics and Computer Science ")
        else:
            print("Not eligible for Science with Mathematics and Computer Science")
    elif grp_op==2:
        if x>=75:
            print("Eligible for Science with Mathematics and Engineering Graphics")
            
        else:
            print("Not eligible for Science with Mathematics and Engineering Graphics")
    elif grp_op==3:
        if x>=70:
            print("Eligible for Science with Biology and Psychology")
        else:
            print("Not eligible for Science with Biology and Psychology")
    elif grp_op==4:
        if x>=65:
            print("Eligible for Commerce with Mathematics and Economics")
        else:
            print("Not eligible for Commerce with Mathematics and Economics")
    elif grp_op==5:
        if x>=60:
            print("Eligible for Commerce with Informatics Practices and Economics")
        else:
            print("Not eligible for Commerce with Informatics Practices and Economics")
    elif grp_op==6:
        if x>=55:
            print("Eligible for Commerce with Marketing and Information Technology")
        else:
            print("Not eligible for Commerce with Marketing and Information Technology")
    elif grp_op==7:
        if x>=50:
            print("Eligible for Humanities with Fine Arts")
        else:
            print("Not eligible for Humanities with Fine Arts")
    elif grp_op==8:
        if x>=45:
            print("Eligible for Humanities without Fine Arts") 
        else:
            print("Not eligible for Humanities without Fine Arts")
    else:
        print("Not eligible for any group")

        
    got7=input("Do you wish to continue checking eligibilty? YES or NO?")
    got7=got7.upper()
    if got7=="YES":
      continue
    elif got7=="NO":
      break

      
#2)a)Read and display all records
def display_Rec():
    f=open("StudentReg.dat","rb")
    print("The student records are:")
    while True:
        try:
            rec=pickle.load(f)
            print("ID no.:", rec['IDNO'])
            print("Name:", rec['NAME'])
            print("Marks:", rec['MARKS'])
            print("Group:",rec['GROUP'])
        except EOFError:
            break
    f.close()
    print()



#2)b)Updating record of marks based on given ID no.
def update_Rec():
    f=open("StudentReg.dat","rb")
    idn=int(input("Enter the ID no. of student to be updated:"))
    m=int(input("Enter the marks of student to be updated:"))
    reclst=[]
    while True:
        try:
            rec=pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    for i in range(len(reclst)):
        if reclst[i]['IDNO']==idn:
            reclst[i]['MARKS']=m
    f=open("StudentReg.dat","wb")
    for x in reclst:
        pickle.dump(x,f)
    print("Record successfully updated")
    f.close()
    print()




#2)c)Searching record based on given ID no.
def search_Rec():
    f=open("StudentReg.dat","rb")
    idno=int(input("Please enter the ID number of the student:"))
    flag=False
    while True:
        try:
            rec=pickle.load(f)
            if rec['IDNO']==idno:
                print("ID no.:", rec['IDNO'])
                print("Name:", rec['NAME'])
                print("Marks:", rec['MARKS'])
                print("Group:",rec['GROUP'])
                flag=True
        except EOFError:
            break
    if flag==False:
        print('Record of student is not found')
    f.close()
    print()





#2)d)Deleting a record based on a given ID no.
def delete_Rec():
  f=open("StudentReg.dat","rb")
  f1=open("StudentReg2.dat","wb")
  idno=int(input("Please enter the ID number of the student you wish to erase from the record"))
  while True:
    try:
      s=pickle.load(f)
      if s['IDNO']!=idno:
        pickle.dump(s,f1)
    except EOFError:
      break
  f.close()
  f1.close()
  os.remove("StudentReg.dat")
  os.rename("StudentReg2.dat", "StudentReg.dat")
  print("Record successfully deleted")
  print()

    
 #3)Fee structure
def display_fee():
  print("FOR SCIENCE STREAM (GROUPS A,B,C):\nQUARTER 1: Rs. 40,000.00 ")
  print("FOR SCIENCE STREAM (GROUPS A,B,C):\nQUARTER 2: Rs. 30,000.00 ")
  print("FOR SCIENCE STREAM (GROUPS A,B,C):\nQUARTER 3: Rs. 30,200.00 ")
  print("FOR SCIENCE STREAM (GROUPS A,B,C):\nQUARTER 4: Rs. 28,000.00")
  print("FOR SCIENCE STREAM (GROUPS A,B,C):\nTotal Yearly Fee: Rs. 1,28,200.00")
  print()
  print("FOR COMMERCE AND HUMANITIES STREAM (GROUPS D,E,F,G,H):\nQUARTER 1: Rs. 30,000.00")
  print("FOR COMMERCE AND HUMANITIES STREAM (GROUPS D,E,F,G,H):\nQUARTER 2: Rs. 25,000.00")
  print("FOR COMMERCE AND HUMANITIES STREAM (GROUPS D,E,F,G,H):\nQUARTER 3: Rs. 28,000.00")
  print("FOR COMMERCE AND HUMANITIES STREAM (GROUPS D,E,F,G,H):\nQUARTER 4: Rs. 25,000.00")
  print("FOR COMMERCE AND HUMANITIES STREAM (GROUPS D,E,F,G,H):\nTotal Yearly Fee: Rs. 1,08,000.00")
  print()




#4)About the academy
def aca_dec():
  print("St.Ives Academy for Higher Learning, since its inception has always strived to create an environment for its inhabitants to bloom into their most prodigious form.")
  print("With utmost care for the students, the interactions students face everyday with is a step forward in their respective roads of success.")
  print("MISSION:\nTo instill within the students the core virtues and create erudite scholars with upstanding and honourable morals. ")
  print("VISION:\nTo become an internationally acclaimed academy for fostering holistic growth")
  print("HISTORY:\nThe foundation stones of the academy was placed on the 15th of March, 1915, as a training camp for recruits to fight in World War 1. With the end of the war, the buildings were converted into the academy that now stands as it is.")
  print("The hallowed walls of this academy has seen the footsteps of some of the most prestigious names to be penned down in the pages of history.\nFrom its humble beginnings of a rather meagre portion of students, to the strength of a hundered thoousand, its growth was only possible due to our founders zeal and confidence.")
  print("Mrs. Emmaline Thrushwright, the very first headmistress of the academy spearheaded the development of the academy, from simple barracks to the castle like building that it is today. The succeding headmasters and headmistresses bulit upon Mrs.Thrushwright's ideas, creating outstanding ,all-rounded, eductional and vocational framework.")
  print("The thousands of students who have graduated bear witness the exceptional fervency of the tutorial faction of the academy in the various fields of Arts, Sciences, Medicine, Engineering, Sports,etc.")
  print("HEADMASTER'S MESSAGE:\nHumbly, I extend my greetings to  one and all and hope that your two years of education at St.Ives Academy for Higher Learning prove to be a simulating and enterprising years. The Academy has always seeks nothing but to bring out the best within each student and foster their talents.")
  print("We provide favourable ambience for the student's education with hands-on learning opportunities for students to gain experience. Our exceptional teaching workforce aims to equip the students with the necessary skills to function as operational members of society.")
  print("We believe in the constant communication between the teaching faculty, the students, and their parents to foster their greatest attributes.")
  print("I hope that together, within these two years, we can create the best image of you for your future and ensure your dreams are realized and take flight within the walls of this hallowed institution.")
  print("Together, towards the future!")
  print()
  
  




#5)Enquiry
def enquiry():
  print("For any enquries or help, please contact our help desk")
  print("CONTACT NUMBER: 9340267893")
  print("EMAIL ADDRESS: helpdesk@stivesaca.com")
  print("SOCIAL MEDIA:\nTwitter: @ST.IVES_Academy1915\nFacebook:@ST.IVES_Academy1915\nInstagram: @ST.IVES_Academy1915")
  print("SCHOOL SITE: www.stivesacademy.com")
  print("The Academy's working hours are:\nMONDAY to FRIDAY: 8:30 am to 4:00 pm")
  print()




#6)Exit code
def exit_code():
  print("Thank you !")
  sys.exit()




#Main menu     
def main_menu():
  while True:
    print()
    print("Please select one of the actions to proceed")
    print("(1)STUDENT REGISTRATION FORM\n(2)STUDENTS DETAILS\n(3)FEE STRUCTURE\n(4)ABOUT ACADEMY\n(5)ENQUIRY\n(6)EXIT")
    c=int(input("Please input your option:"))
    if c==1:
      stu_add()
    elif c==3:
      display_fee()
    elif c==2:
      sub_menu()
    elif c==4:
      aca_dec()
    elif c==5:
      enquiry()
    elif c==6:
      exit_code()
    got=input("Do you wish to continue,YES or NO?")
    got=got.upper()
    if got=="YES":
      continue
    elif got=="NO":
      sys.exit()
    else:
      print("Invalid choice")  
  
  
  
  #Sub menu
def sub_menu():
  while True:
    print()
    print("Please select one of the actions to proceed")
    print("1)DISPLAY ALL STUDENT RECORDS\n2)UPDATE STUDENT MARKS\n3)SEARCH FOR STUDENT RECORD\n4)DELETE STUDENT RECORD\nENTER 0 TO PROCEED BACK TO MAIN MENU")
    ch=int(input("Please input your option:"))
    if ch==1:
      display_Rec()  
    elif ch==2:
      update_Rec() 
    elif ch==3:
      search_Rec()
    elif ch==4:
      delete_Rec()
    elif ch==0:
      main_menu()
    else:
      print("Invalid option")



#Main function call/Main code
print("Welcome to St.Ives Academy for Higher Learning")
main_menu()     