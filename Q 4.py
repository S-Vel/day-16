#Q4.Write a Python program to find numbers divisible by 9 from a list of numbers 

l=[9,18,20,27,30]
f=tuple(filter(lambda x:(x%9==0),l))
print("Elemens divisible by 9 : ",f)
print()
