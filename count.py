n=int(input("Enter any value="))
count=0
while n>0:
    count=count+1
    print("n=",n)
    n=n//10
print("No of digits=",count)
