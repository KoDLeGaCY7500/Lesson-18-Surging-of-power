# def compute(x,y):
#     result=1
#     while y>0:
#         if y%2==0:
#            x=x*x
#            y>>=1
#         else:
#             result=result*x
#             y=y-1
#     return result

# x=int(input("enter no: "))
# y=int(input("enter power: "))

# print(compute(x,y))

def power2(number):
    if number <=0:
        return False
    return(number&(number-1))==0

n=int(input("enter number: "))

if power2(n):
    print("number is the power of 2")
else:
    print("number is not a power of 2")

