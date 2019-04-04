num=int(input("Enter a number: "))
rev=0
temp=num
while (temp>0) :
    x=temp%10
    rev=rev*10+x
    temp//=10

if (num==rev) :
    print("{} is a palindrome number.".format(num))
else :
    print("{} is not a palindrome number.".format(num))
    
