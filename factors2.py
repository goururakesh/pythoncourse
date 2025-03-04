n=int(input("Enter any value="))
i=1
count=0
print("Factor of {} are=".format(n))
while i<=n:
    if n%i==0:
        print(i)
        count=count+1

    i=i+1
print("No. of factors =",count)
