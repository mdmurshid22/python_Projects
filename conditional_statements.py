#1)Find the greatest number of given three nuumber?
'''num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=int(input("Enter Third Number:"))
if (num1 > num2) & (num1 > num3):
	print("First Numbers is Greater:",num1)
elif num2>num3:
	print("Second Number is Greater:",num2)
else:
	print("Third Number is Greater:",num3)'''

#2)Polindrome?
'''s=input("Enter Some String:")
s1=s[::-1]
if s == s1:
	print("It is Polindrome:",s)
else:
	print("It is not a Polindrome:",s)'''

#Voting?
'''age=int(input("Enter Your Age:"))
if age >= 18:
	print("You are Eligible for voting:",age)
else:
	print("You are not Eligible for Voting:",age)'''

#Pass or Fail program?
'''tamil=int(input("Enter Tamil Mark:"))
english=int(input("Enter English Mark:"))
maths=int(input("Enter Maths Mark:"))
science=int(input("Enter Science Mark:"))
social=int(input("Enter Social Mark:"))
if tamil >=35:
	if english >=35:
 		if maths >=35:
 			if science >=35:
 				if social >=53:
 					print("Tamil:{} pass\nEnglish:{} pass\nMaths:{} pass\nScience:{} pass\nSocial:{} pass".format(tamil,english,maths,science,social))
 					print("Total Marks:{}".format(tamil+english+maths+science+social))
 					print("Percentage of All Subjects is:{:.1f}%".format(tamil,english,maths,science,social/500*100))
else:
	print("Fail\nTamil:{}\nEnglish:{}\nMaths:{}\nScience:{}\nSocial:{}".format(tamil,english,maths,science,social))'''
'''import math
d=dir(math)
for x in d:
	print(x)'''
num=int(input("How Many Subject Marks Do You Want:"))
list=["Tamil","English","Maths","Science","Social"]
for i in range(num):
	l=[]
	student_name=input("Enter Student Name:")
	for x in range(5):
		subject=int(input("Enter {} Mark:".format(list[x])))
		l.append(subject)
		output=sum(l)
	print("Total Marks {} By {}".format(output,student_name))
	print()