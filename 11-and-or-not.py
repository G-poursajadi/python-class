
# and
age=int(input("sen khod ra vared konid  "))
jensiat = str(input("pesar ya dokhtar"))
tahsilat = str(input("da hah tahsil ya etmam tahsil"))
if age>=18 and jensiat=="pesa" and tahsilat=="etmam tahsil" :
    print(" shoma mashmol sarbazi hastid")
else:
    print("  mashmol sarbazi nisti :) ")


# or
hava=str(input("aftabi ya abri ya barfi"))
if hava=="aftabi" or hava=="abri" :
    print("berim biron")
else :
    print(" bemonim khone")

# not
x=True
print(x)
print(not x)