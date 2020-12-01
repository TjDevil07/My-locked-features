



def strrevword(str1):
   str3=""
   str2=str1.split( )
   str2=str2[::-1]
   for i in str2 :
      if str3=="":
         str3=i
      else:
         str3=str3+" "+i
   print(str3)

def suma(n):
   if n==1:
      return (1)
   else :
      return(n+suma(n-1))

   
def strback(str1,n):
   if n>0:
      print(str1[n],end=' ')
      strback(str1,n-1)
   elif n==0 :
      print(str1[0])



#main()
import time
import accdel
U_F=open(r'D:\Access\user.txt','r')
P_F=open(r'D:\Access\password.txt','r')
strU=U_F.readlines()
strP=P_F.readlines()
strU=strU[0]
strP=strP[0]
strU=strU.split(' ')
strP=strP.split(' ')
U_F.close()
P_F.close()
a1=0
a2=0
az='N'
ay=0
n='N'
lcU=len(strU)
lcP=len(strP)
if lcU == lcP:
    lc=lcU
    print ("Starting Program")
    U=input("Username : ")
    P=input("Password = ")
    if U == strU[0] and P == strP[0]:
        a1=time.time()
        a2=time.ctime(a1)
        print ("------------------------------------------------------------------------------")
        print (a2) 
        while n == 'N':
            print ("------------------------------------------------------------------------------------")
            print ("                        Welcome to the Python world")
            print ("                        ------- -- --- ------ -----")
            print ('\n')
            print ('logout : L')
            print ('\n')
            print (" options")
            print (" -------")
            print ('\n')
            print (" want to add password and username = A")
            print 
            print (" sum recursion = sr")
            print
            print (" string sentense reverse program = revsentence")
            print 
            print (" string word reverse program = revstring")
            print 
            print (" want to delete account = Z")
            print ('\n')
            print ("------------------------------------------------------------------------------------")
            print ('\n')

            t=input(" what do you want? = ")

            if t=="A" :
                 p=input(" new username = ")
                 q=input(" new password = ")
                 U_F=open(r'D:\Access\user.txt','a')
                 P_F=open(r'D:\Access\password.txt','a')
                 U_F.write(" ")
                 U_F.write(p)
                 P_F.write(" ")
                 P_F.write(q)
                 U_F.close()
                 P_F.close()
            elif t=="Z":
                 accdel.a()
            elif t=="L":
                 n="L"
            elif t=='sr':
                while az=='N':
                    x=int(input("enter any no. = "))
                    print (suma(x))
                    ay=input('')
                    az=input("Proceed to next command Y/N : ")
            elif t=='revsentence' :
                while az=='N':
                    x=input("any any string = ")
                    strrevword(x)
                    ay=input('')
                    az=input("Proceed to next command Y/N : ")
            elif t=='revstring' :
                while az=='N':
                    s=input('Enter a string = ')
                    ay=input('')
                    strback(s,len(s)-1)
                    ay=input('')
                    az=input("Proceed to next command Y/N : ")
    
        else:
            print ("------------------------------------------------------------------------------")
            print ('Logged out')
            b1=time.time()
            b2=time.ctime(a1)
            print (b2)
            print ('time elapsed :',b1-a1,'secs')
            print ("------------------------------------------------------------------------------")            
        
    else :
        for i in range(1,lc):
            if U == strU[i] and P == strP[i]:
                a1=time.time()
                a2=time.ctime(a1)
                print ("------------------------------------------------------------------------------")
                print (a2)
                while n == 'N':
                    print ("------------------------------------------------------------------------------")
                    print ("                        Welcome to the Python world")
                    print ("                        ------- -- --- ------ -----")
                    print ('\n')
                    print ('logout : L')
                    print ('\n')
                    print (" options")
                    print (" -------")
                    print ('\n')
                    print (" want to add password and username = A")
                    print 
                    print (" sum recursion = sr")
                    print
                    print (" string sentense reverse program = revsentence")
                    print 
                    print (" string word reverse program = revstring")
                    print 
                    print (" want to delete account = Z")
                    print ('\n')
                    print ("------------------------------------------------------------------------------")
                    print ('\n')

                    t=input(" what do you want? = ")

                    if t=="A" :
                             p=input(" new username = ")
                             q=input(" new password = ")
                             U_F=open(r'D:\Access\user.txt','a')
                             P_F=open(r'D:\Access\password.txt','a')
                             U_F.write(" ")
                             U_F.write(p)
                             P_F.write(" ")
                             P_F.write(q)
                             U_F.close()
                             P_F.close()
                    elif t=="Z":
                         accdel.a()
                    elif t=="L":
                         n="L"
                    elif t=='sr':
                        while az=='N':
                            x=int(input("enter any no. = "))
                            print (suma(x))
                            ay=input('')
                            z=input("Proceed to next command Y/N : ")
                            az=input("Proceed to next command Y/N : ")
                    elif t=='revsentence' :
                        while az=='N':
                            x=input("any any string = ")
                            strrevword(x)
                            ay=input('')
                            az=input("Proceed to next command Y/N : ")
                    elif t=='revstring' :
                        while az=='N':
                            s=input('Enter a string = ')
                            strback(s,len(s)-1)
                            ay=input('')
                            az=input("Proceed to next command Y/N : ")
                            
                else:
                    print ("------------------------------------------------------------------------------")
                    print ('Logged out')
                    b1=time.time()
                    b2=time.ctime(a1)
                    print (b2)
                    print ('time elapsed :',b1-a1,'secs')
                    print ("------------------------------------------------------------------------------")
                    break
        else :
            print (' incorrect username or password')
else:
    print('Program error')
