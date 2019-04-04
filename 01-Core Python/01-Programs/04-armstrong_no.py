num=int(input("Enter A Number: "))
sum=0
temp= num
while temp>0:
    x=temp%10
    sum+=x**3
    temp//=10
    
if num==sum :
    print("{} is an Armstrong number.".format(num))
else :
    print("{} is not an Armstrong number.".format(num))


