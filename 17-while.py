# یک بولین به حلقه یده
#  برنامه ای بنوسید که تا زمانی که پسورد آن درست نباشد برنامه ادامه پیدا نکند

number_faild = 0
password = input("lotfan password khod ra vared konid")
while password != 12345 :
    print("password eshtebahe")
    number_faild += 1
    
    password = input("dobare passwoed khod ra vared jkonid")
print("vared shodid")

# mesal
# x=1
# while x<10 :
#     print(x)
#     x +=1