def add(x,y):
    return x+y
def mul(x,y):
    return x*y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y
print("what function u like to do")
print("1 for add")
print("2 for mul")
print("3 for sub")
print("4 for div")

solution = input("enter ur choice:")

a=int(input("enter ur 1st number"))
b=int(input("enter ur 2nd numbet"))

if solution=='1':
    print(a,"+",b,"="addittion(a,b))
elif solution=='2':
    print(a,"-"b,"="sub(a,b))
elif soluition=='3':
    print(a,"*",b,"="mul(a,b))
elif solution=='4':
    print(a,"/",b,"="div(a,b))
      
