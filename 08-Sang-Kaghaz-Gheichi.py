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
elif player1 == "sang" and player2 =="gheichi" :
    print("Player1 win")
elif player1 == "kaghaz" and player2 =="sang" :
    print("Player1 win")
elif player1 == "kaghaz" and player2 =="gheichi" :
    print("Player2 win")
elif player1 == "gheichi" and player2 =="sang" :
    print("Player2 win")
elif player1 == "gheichi" and player2 =="kaghaz" :
    print("Player1 win")
else :
    print("Harekat shoma eshtebah mibashad")