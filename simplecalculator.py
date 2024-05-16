#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2



#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3






#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
History=[]
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  print("8.History  : ? ")
  
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
  print(choice)
  if choice=="#":
    #program ends here
    print("Done. Terminating")
    exit()
  else:
      
      if choice=="+":
         num1=input()
         print("Enter first number:",num1)
         if num1=="0$":
                 continue
         if num1=="#":
             print("Done. Terminating")
             exit()
         num2=input()
         print("Enter second number:",num2)
         if num2=="0$":
                 continue
         if num2=="#":
             print("Done. Terminating")
             exit()
         p=float(num1)+float(num2)
         print(float(num1),choice,float(num2),"=",float(p))
         new=float(num1),choice,float(num2),"=",float(p)
         x1=new[0]
         x2=new[1]
         x3=new[2]
         x4=new[3]
         x5=new[4]
         History.append(str(x1)+" "+str(x2)+" "+str(x3)+" "+str(x4)+" "+str(x5))

      if choice=="-":
         num1=input()
         print("Enter first number:",num1)
         if num1=="0$":
                 continue
         if num1=="#":
             print("Done. Terminating")
             exit()
         num2=input()
         print("Enter second number:",num2)
         if num2=="0$":
                 continue
         if num2=="#":
             print("Done. Terminating")
             exit()
         p=float(num1)-float(num2)
         print(float(num1),choice,float(num2),"=",float(p))
         new=float(num1),choice,float(num2),"=",float(p)
         x1=new[0]
         x2=new[1]
         x3=new[2]
         x4=new[3]
         x5=new[4]
         History.append(str(x1)+" "+str(x2)+" "+str(x3)+" "+str(x4)+" "+str(x5))
      if choice=="*":
         num1=float(input())
         print("Enter first number:",num1)
         if num1=="0$":
                 continue
         if num1=="#":
             print("Done. Terminating")
             exit()
         num2=float(input())
         print("Enter second number:",num2)
         if num2=="0$":
                 continue
         if num2=="#":
             print("Done. Terminating")
             exit()
         p=float(num1)*float(num2)
         print(float(num1),choice,float(num2),"=",float(p))
         new=float(num1),choice,float(num2),"=",float(p)
         x1=new[0]
         x2=new[1]
         x3=new[2]
         x4=new[3]
         x5=new[4]
         History.append(str(x1)+" "+str(x2)+" "+str(x3)+" "+str(x4)+" "+str(x5))
      if choice=="/":
         num1=input()
         print("Enter first number:",num1)
         if num1=="0$":
                 continue
         num2=input()
         print("Enter second number:",num2)
         if num2=="0":
             print("float division by zero")
             print(float(num1),"/",float(num2),"= None")
             new=float(num1),"/",float(num2),"= None"
             new=float(num1),choice,float(num2),"=","None"
             x1=new[0]
             x2=new[1]
             x3=new[2]
             x4=new[3]
             x5=new[4]
             History.append(str(x1)+" "+str(x2)+" "+str(x3)+" "+str(x4)+" "+str(x5))
         else:
             if num2=="0$":
                 continue
             else:
                  p=float(num1)/float(num2)
                  print(float(num1),choice,float(num2),"=",p)
                  new=float(num1),choice,float(num2),"=",p
                  new=float(num1),choice,float(num2),"=",float(p)
                  x1=new[0]
                  x2=new[1]
                  x3=new[2]
                  x4=new[3]
                  x5=new[4]
                  History.append(str(x1)+" "+str(x2)+" "+str(x3)+" "+str(x4)+" "+str(x5))
         
           
      if choice=="^":
         num1=float(input())
         print("Enter first number:",num1)
         if num1=="0$":
                 continue
         if num1=="#":
             print("Done. Terminating")
             exit()
         num2=float(input())
         print("Enter second number:",num2)
         if num2=="0$":
                 continue
         if num2=="#":
             print("Done. Terminating")
             exit()
         p=float(num1)^float(num2)
         print(float(num1),choice,float(num2),"=",float(p))
         new=float(num1),choice,float(num2),"=",float(p)
         x1=new[0]
         x2=new[1]
         x3=new[2]
         x4=new[3]
         x5=new[4]
         History.append(str(x1)+" "+str(x2)+" "+str(x3)+" "+str(x4)+" "+str(x5))

      if choice=="%":
         num1=float(input())
         print("Enter first number:",num1)
         if num1=="0$":
                 continue
         if num1=="#":
             print("Done. Terminating")
             exit()
         num2=float(input())
         print("Enter second number:",num2)
         if num2=="0$":
                 continue
         if num2=="#":
             print("Done. Terminating")
             exit()
         p=float(num1)%float(num2)
         print(float(num1),choice,float(num2),"=",float(p))
         new=float(num1),choice,float(num2),"=",float(p)
         x1=new[0]
         x2=new[1]
         x3=new[2]
         x4=new[3]
         x5=new[4]
         History.append(str(x1)+" "+str(x2)+" "+str(x3)+" "+str(x4)+" "+str(x5))

      if choice=="?":
          if History==[]:
            print("No past calculations to show")
          else:
               for i in History:
                    print(i)
          
       