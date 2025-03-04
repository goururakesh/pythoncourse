n=int(input("Enter any value="))
i=1
print("Factors of {} are=".format(n))
while i<=n:
    if n%i==0:
        print(i)
    i=i+1
