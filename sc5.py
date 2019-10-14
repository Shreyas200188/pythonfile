i=1500
print("No.s required between 1500 and 2700 : ",) 
while i<= 2700:
	if(i%7==0 and i%5==0):
		print(i)
	i=i+1

print()


a=input("Enter a string : ")
cnum=0
calp=0
i=0
while i < len(a):
	if(ord(a[i])>=48 and ord(a[i])<=57 ):
		cnum += 1
	elif ((ord(a[i])>=65 and ord(a[i])<=90) or (ord(a[i])>=97 and  ord(a[i])<=122)):
		calp += 1
	else:
		pass
	i+=1
print("No. of alphabets =",calp)
print("NO.of numbers =",cnum)


print()



a=input("Enter password = ")
i=0
cnum=0
csml=0
ccap=0
spl=[]
while(i<len(a)):
	if(ord(a[i])>=48 and ord(a[i])<=57 ):
		 cnum += 1
	elif (ord(a[i])>=65 and ord(a[i])<=90):
		ccap += 1
	elif (ord(a[i])>=97 and ord(a[i])<=122):
		csml +=1 
	else:
		spl.append(a[i])
	i=i+1
if(cnum>=1 and ccap>=1 and csml>=1 and len(a)>=6 and len(a)<=16 and ('@'in spl or '#'in spl or'$' in spl)):
	print("Valid password")
else:
	print("Invalid password")


print()


a=int(input("Enter 1st no : "))
b=int(input("Enter 2nd no : "))
if(a>b):
	num1=a
	num2=b
else:
	num1=b
	num2=a
d=num1%num2
while(d!=0):
	num1=num2
	num2=d
	d=num1%num2
print("HCF = ",num2)
print("LCM = ",(a*b/num2))


