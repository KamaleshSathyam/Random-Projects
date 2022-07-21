
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
print("Enter the operator you want to perform");
ch=input("Enter any of these operator +, -, *, /  ")

if ch=='+':
    result=n1+n2;
elif ch=='-':
    result=n1-n2;
elif ch=='*':
    result=n1*n2;
elif ch=='/':
    result=n1/n2;
else:
   print("char is not supported");
print(n1,ch,n2,"= ",result)