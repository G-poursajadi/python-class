num1 = float(input(" please wright first Number"))
num2 = float(input(" please wright secound Number"))
operation = input("please write your operation")
if operation =="+":
    # answer = num1 + num2
    print(num1 + num2)
elif operation =="-":
    print(num1 - num2)
elif operation =="/":
    print(num1/num2)
elif operation =="*":
    print(num1*num2)
else:
    print("program cant find this operation")