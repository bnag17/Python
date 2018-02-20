import random
l=["rock","paper","scissor"]
comp=random.choice(l)
user=input("enter your choice:")
print("computer=",comp)
if comp==user:
   print("it is a tie game")
elif comp=="rock" and user=="scissor":
   print("computer has bet u with rock.")
elif comp=="scissor" and user=="paper":
   print("computer has cut u with scissor")
elif comp=="paper" and user=="rock":
    print("computer is caught u with paper")
else:
    print("you won upon computer")
