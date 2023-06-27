# کاری کنید بازی سنگ کاغذ قیچی تا امتیاز 3 اتفاق بیافتد
# ctrl +[ or ] کد ها زیر مجموعه کد های بالایی می شوند

emtiazeP1 = 0
emtiazeP2 = 0

while emtiazeP1<=3 and emtiazeP2<=3:
    import random
    print("Sang,Kaghaz,Gheichi")

    player1 = input ("Harekat khod ra vared konid:").lower()
    # player2 = input ("Harekat khod ra vared konid:").lower()

    randomnum = random.randint(1,3)
    if randomnum == 1 :
        player2 = "sang"
    elif randomnum == 2 :
        player2 = "kaghaz"
    elif randomnum == 3 :
        player2 = "gheichi"
    print(player2)



    if player1 == player2 :
        print("Mosavi")
    elif player1 == "sang" and player2 =="kaghaz" :
        print("Player2 win")
        emtiazeP2 +=1
    elif player1 == "sang" and player2 =="gheichi" :
        print("Player1 win")
        emtiazeP1 +=1
    elif player1 == "kaghaz" and player2 =="sang" :
        print("Player1 win")
        emtiazeP1 +=1
    elif player1 == "kaghaz" and player2 =="gheichi" :
        print("Player2 win")
        emtiazeP2 +=1
    elif player1 == "gheichi" and player2 =="sang" :
        print("Player2 win")
        emtiazeP2 +=1
    elif player1 == "gheichi" and player2 =="kaghaz" :
        print("Player1 win")
        emtiazeP1 +=1
    else :
        print("Harekat shoma eshtebah mibashad")

print("\n")
print(f"emtize player 1 : {emtiazeP1}")
print(f"emtize player 2 : {emtiazeP2}")
