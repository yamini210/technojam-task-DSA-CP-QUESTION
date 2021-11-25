N=int(input("enter a number on which you want to want to perform subtraction \n"))
k=int(input("slkdjfalkjsd"))

i=0

if(N>=2 and N<=pow(10,9)and k>=1 and k<=50):
    for i in range(k):
        if(N%10!=0):
            N=N-1
        else:
            N=N/10
    print("number after",k,"subtraction is",int(N))
else:
    print("Constraints are not matching")
    
    
   


    
