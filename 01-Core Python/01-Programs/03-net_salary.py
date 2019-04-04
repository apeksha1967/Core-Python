bs = int(input("Enter basic salary: "))
hra= bs*30/100
da= bs*20/100
ta= bs*10/100
a= hra+da+ta
pf= 1400
ns= bs+a-pf
print("""
HRA = {}
DA = {}
TA = {}
NET SALARY = {}
""".format(hra,da,ta,ns))
