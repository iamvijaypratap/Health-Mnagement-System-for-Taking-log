import datetime
#def time():
  # return datetime.datetime.now()
dt = datetime.datetime.now() 
def Entry(filename):
    with open (filename ,'a') as f:
        inp = input("Type Here : \n")
        #f.write(f"{time()} {inp}")
        f.write(dt.strftime ("%A %d %b %Y , %I : %M %p") + inp + "\n" )
def rtrv(filename):
    with open (filename) as f:
        print(f.read())
def health(take):
#for client 1
#client1 log
    if take=="client1":
       a = input("What Do You Want Sir : Log Or Retrieve ? \n")
       if a=="log":
          print("Sir Which Type Of log ? : Food or Exercise ? :")
          o =input("Type here :\n")
          if o=="food":
            print("Enter Food You Have Eaten Sir")
            #d=str(input("Type Here : \n"))
            #with open ('client_1.txt','a') as f:
             #   f.write(str([str(time())]) + ":" +d+"\n")
            Entry('client_1.txt')
            print("Successfully Submited !")
          if o=="exercise":
            print("Which Type Of Exercise Sir ?")
            #g=str(input("Type Here : \n"))
            #with open ('client_1_ex.txt','a') as f:
             #  f.write(str([str(time())]) + ":" +g+"\n")
            Entry('client_1_ex.txt')
            print("Successfully Submited")  

#client 1 retrieve
       if a=="retrieve":
          print("Food or Exercise ? :")
          m=input("Type here :\n")
          if m=="food":
            #with open ('client_1.txt') as f:
             #  z=str(f.read())
              # print(z)
            rtrv('client_1.txt')
          if m=="exercise":
            #with open ('client_1_ex.txt') as f:
             #  x=str(f.read())
              # print(x)
             rtrv('client_1_ex.txt')
         

#for client 2 
##client 2 log entry
    if take=="client2":
       b = input("What Do You Want Sir : Log Or Retrieve ? \n")
       if b=="log":
          print("Sir Which Type Of log ? : Food or Exercise ? :")
          p=input("Type here :\n")
          if p=="food":
               print("Enter Food You Have Eaten Sir")
              # n=str(input("Type Here : \n"))
              # with open ('client_2.txt','a') as f:
               #     f.write(str([str(time())]) + ":" +n+"\n")
               Entry('client_2.txt')
               print("Successfully Submited !")
          if p=="exercise":
               print("Which Type Of Exercise Sir ?")
              # h=str(input("Type Here : \n"))
              # with open ('client_2_ex.txt','a') as f:
               #     f.write(str([str(time())]) + ":" +h+"\n")
               Entry('client_2_ex.txt')
               print("Successfully Submited")   

#client 2 retrieve
       if b=="retrieve":
          print("Food or Exercise ? :")
          q=input("Type here :\n")
          if q=="food":
             #with open ('client_2.txt') as f:
              # s=str(f.read())
               #print(s)
            rtrv('client_2.txt')
          if q=="exercise":
             #with open ('client_2_ex.txt') as f:
              # r=str(f.read())
               #print(r)
            rtrv('client_2_ex.txt')

#for client 3
#client 3 log entry
    if take=="client3":
       c = input("What Do You Want Sir : Log Or Retrieve ? \n")
       if c=="log":
          print("Sir Which Type Of log ? : Food or Exercise ? :")
          w=input("Type here :\n")
          if w=="food":
               print("Enter Food You Have Eaten Sir")
               #l=str(input("Type Here : \n"))
               #with open ('client_3.txt','a') as f:
                #    f.write(str([str(time())]) + ":" +l+"\n")
               Entry('client_3.txt')
               print("Successfully Submited !")
          if w=="exercise":
               print("Which Type Of Exercise Sir ?")
              # v=str(input("Type Here : \n"))
               #with open ('client_3_ex.txt','a') as f:
                #    f.write(str([str(time())]) + ":" +v+"\n")
               Entry('client_3_ex.txt')
               print("Successfully Submited")   

#client 3 retrieve
       if c=="retrieve":
          print("Food or Exercise ? :")
          t=input("Type here :\n")
          if t=="food":
             #with open ('client_3.txt') as f:
              # x=str(f.read())
               #print(x)
            rtrv('client_3.txt')
          if t=="exercise":
             #with open ('client_3_ex.txt') as f:
              # u=str(f.read())
               #print(u)
            rtrv('client_3_ex.txt')        
#loop 
while True:
      print(''' Hello Sir , i am your Health Manager , i will keep an Eye on Your Health information.
     if you want to add or Retrieve some Logs , Select from Given Options''')
      ta = input("Hello sir Let Me Know WHO YOU ARE ? : Our Client 1 or Client 2 or Client 3 ? \n")
      health(ta)
      
      choice = input("Do You Want To Add Some More Logs : ? yes/no \n") 
      if choice=="yes":
         continue
      else:
         print("Thank You For Using Our Health Management System")
         break
