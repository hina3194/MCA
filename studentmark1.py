def studentBasicDetails():
        name=input("enter student name")
        CourseDetails=input("enter the course in which student is study")
        Regno=input("enter registration no")
        Fathername=input("enter father name")
        Mothername=("enter the mother name")
        adress=input("enter the adress of student")
        DOB=input("enter the date of birth")



        details={"Name:":name,"Course:":CourseDetails,"RegNo:":Regno,"FatherName:":Fathername,"MotherName":Mothername,"Adress:":adress,"Date:":DOB}
         
        for k,v in details.items():
              print(k,v)
        
studentBasicDetails()



def subjectMarks():

        for i in range(5):
        
                print("subject marks:",i+1)
                CA=int(input("Enter your ca marks"))
                if CA>30:
                    print("marks should not be greater than 30:")
                    CA=int(input("Enter your ca marks out of 30"))
                MidTerm=int(input("enter your mid term marks"))
                if MidTerm>50:
                    print("marks should not be greater than 50:")
                    MidTerm=int(input("Enter your mid term marks out of 50"))
                EndTerm=int(input("enter your end term marks"))
                if EndTerm >100:
                    print("marks should not be greater than 100:")
                    CA=int(input("Enter your end term marks out of 100"))
                Attendence=int(input("enter your attendence:"))
                if Attendence>5:
                    print("marks should not be greater than 5")
                    Attendence=int(input("enter your attendence: out of 5"))
                finalMarks=CA+MidTerm+EndTerm+Attendence;
                print("final marks is",finalMarks)
                #display=tabulate([["Continous","midterm","end","attendence"][CA,MidTerm,EndTerm,Attendence]
    

                
            
