a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if (a==b and b==c):
    print("all are equal")
elif a>b>c:
    print("a is greatest")
elif b>a>c:
    print("b is greatest")
elif c>b>c:
    print("c is greatest")
else:
    print("false conditon")              