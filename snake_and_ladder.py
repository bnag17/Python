import random#extracting random function
count=0
while(count<=100):
    a=input("Enter 'r' to roll a dice")
    if(a=='r'):
        r= random.randint(1,6)#printing random number from 1 to 6.
        count=count+r
        print("Dice value=")
        print(r)
        print("count value=")
        print(count)
        
    elif (count ==8):#if condition
        count=37
        print("you have climbed the ladder")
    elif (count ==13):
        count=34
        print("you have climbed the ladder")
    elif (count ==40):
        count=68
        print("you have climbed the ladder")
    elif (count ==52):
        count=81
        print("you have climbed the ladder")
    elif (count ==76):
        count=97
        print("you have climbed the ladder")
    elif (count ==11):
        count=2
        print("you have caught by snake")
    elif (count ==25):
        count=4
        print("you have caught by snake")
    elif (count ==38):
        count=9
        print("you have caught by snake")
    elif (count ==65):
        count=46
        print("you have caught by snake")
    elif (count ==89):
        count=70
        print("you have caught by snake")
    elif (count ==93):
        count=64
        print("you have caught by snake")
    else:
        if c==100:
            print("you have won the game")
        
