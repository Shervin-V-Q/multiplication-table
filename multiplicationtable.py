a= int(input("write first number:"))
b= int(input("write second number:"))
c=a*b
d=input("do you want to add number? yes/no?")
while d=="yes":
    z=int(input("write number:"))
    c=c*z
    d=input("do you want to add number? yes/no?")
print(f"result of multiplication is {c}")