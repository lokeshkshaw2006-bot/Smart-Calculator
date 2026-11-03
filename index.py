def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def mod(a,b):
    return a%b

def div(a,b):
    return a/b

def pow(a,b):
    return a**b

a = float(input("Enter first element :"))
o = input("Operation :")
b = float(input("Enter second element :"))

print("ans : ")
if(o == '+'):
    print(sum(a,b))
elif(o == '-'):
    print(sub(a,b))
elif(o == '*'):
    print(mul(a,b))
elif( o== '/'):
    print(div(a,b))
elif(o == '%'):
    print(mod(a,b))
elif(o == '^'):
    print(pow(a,b))
