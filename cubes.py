n=int(input("Enter any value="))
sum=0
while n>0:
    r=n%10
    sum=sum+r*r*r
    n=n//10
print("sum of cubes of digits=",sum)
