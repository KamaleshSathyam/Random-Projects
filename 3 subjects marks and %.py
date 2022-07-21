mark1 = int (input ("Enter the mark for subject 1 :- "))
mark2 = int (input ("Enter the mark for subject 2 :- "))
mark3 = int (input ("Enter the mark for subject 3 :- "))
print ("Average marks is :- ", (mark1 + mark2 + mark3) / 3 )
per = ((mark1 + mark2 + mark3) / 300) * 100
print("Percentage :-",per)
if per >= 90 :
    print ("Grade is 'A'")
elif per >= 80 and per <= 90 :
    print ("Grade is 'B'")
elif per >= 65 and per <= 80 :
    print ("Grade is 'C'")
elif per >= 40 and per <= 65 :
    print ("Grade is 'D'")

elif per <= 40 :
    print ("Grade is 'Fail'")20
    
