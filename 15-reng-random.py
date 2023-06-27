# range(1,1001)
# 1 TA 100
print("range")
for anyNumber in range(1,1001):
    print(anyNumber)
# rangbaraye namayesh fasele haie 2ta 2ta ya 3ta 3ta va.....
# faght baiad pass adade enthaie range yek "," bezarim va faseele mored nazar ra benivisim.
# print(range(5,100,3)) >> kar nakard
# print(range(5,0.-1))

# # adade mojod bein do adad sahih random
print("adade mojod bein do adad sahih random")
import random
randomN1 = random.randint (1,100)
randomN2 = random.randint (100,200)
print(randomN1 , randomN2)
for anyNumber in range(randomN1,randomN2) :
    print(anyNumber)


# بخش پذیری بر 3 یا 5
# جمع اعدادی که بر 3 یا 5 بخش پذیرند برای اعداد زیر 100 را بیابید
print("bakhsh paziri bar 3 va 5")
jam = 0
n = 100
rangeN = range(1,n)
for anyNumber in rangeN :
    if anyNumber % 3==0 or anyNumber % 5==0 :
        jam = jam + anyNumber
print(jam)
