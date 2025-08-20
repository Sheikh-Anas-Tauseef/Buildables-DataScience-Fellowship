n=int(input("How many Terms?"))
a,b=0,1
print("Fibonacci Sequence:")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
