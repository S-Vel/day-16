#Q5.Write a Python program to count the even numbers in a given list of integers 

l1=[9,18,20,27,30,2,3,4,5,66,7]
f1=tuple(filter(lambda x:(x%2==0),l1))
print("number of even elements : ",len(f1))
