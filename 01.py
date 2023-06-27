#1.try following mathematical alucation and guess what is happenin
#((3/2)) --> 1.5  -->1.5
#((3//2)) -->?    -->1
#((3%2)) -->0.06  -->1
#((3**2)) -->9    -->9

a = 3
b = 2
print((a/b))
print((a//b))
print((a%b))
print((a**b))

#suggestin : check the python library refrenve at :
#http://docs.org/3/library/

#2.calculate the average of the following sequenves of numbers
#(2,4)  -->3  ,  (4,8,9)  -->7  ,  (12,14/6,15)   -->13.86

# a =(2,4)
# b =(4,8,9)
# c =(12,14.6,15)

print((2+4)/2)
print((4+8+9)/3)
print((12+14.6+15)/3)

#3.(4/3 * PI * r**3)
#r=5    ,PI=3.1415   --> 523.5

r=5
PI=3.1415
print(4/3 * PI * r**3)


#4.use the modulo oerator (%) to chech odd and even numbers
#(1,5,20,60,7)

num = int(input(1,5,20,60,7))
if (num/2) == 0:
    print("{0} is even nuber". format(num))
else:
    print("{0} is odd nuber". format(num))
 
