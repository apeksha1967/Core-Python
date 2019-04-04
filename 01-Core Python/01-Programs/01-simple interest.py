principal = int(input("Enter Principal amount: "))
rate = float(input("Enter rate of interest(%): "))
x = int(input("years: "))
y = int(input("months: "))
time = x+y/12
print("Time: ",time)
SI= principal*rate/100*time
print("Simple Interest = ",SI)
amount= principal+SI
print("Final Amount = ",amount)
