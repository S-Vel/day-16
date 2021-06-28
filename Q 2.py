#Q2.Write a Python program to create Fibonacci series to n using Lambda

n=int(input("Enter number of elements in fibonacci series "))
lst=[0,1]
y=lambda c,d:int(c+d)
print(lst[0],"",lst[1],end=" ")
for i in range(n-2):
    z=y(lst[i],lst[i+1])
    print(z,end=" ")
    lst.append(z)
print()
