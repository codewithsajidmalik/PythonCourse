import random
# 1 for snake
# -1 for water
# 0 for gun

computer = random.choice([1,-1,0])
youstr = input("Enter you choice: ")
youdic = {"s":1,"w":-1,"g":0}
revrseDic = {1:"s",-1:"w",0:"g"}
you = youdic[youstr]

print(f"you choose {revrseDic[you]}\ncomputer choose {revrseDic[computer]}")

if(computer == you):
    print("its draw")
    
else:
    if(computer ==-1 and you ==1):
        print("you win!")
    elif(computer ==-1 and you ==0):
            print("you loose")
    elif(computer ==1 and you ==-1):
                print("you loose")
            
    elif(computer ==1 and you ==0):
                    print("you win!")
    elif(computer ==0 and you ==-1):
                        print("you win")
    elif(computer ==0 and you ==1):
                            print("you loose")
    else:
        print("oops wrong choose!")


