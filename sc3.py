a=float(input("Enter 1st no = "))
b=float(input("2nd no = "))
def opr(num1,num2) :
	print(num1," + ",num2," = ",num1+num2)
	print(num1," / ",num2," = ",num1/num2)
	print(num1," // ",num2," = ",num1//num2)
	print(num1," * ",num2," = ",num1*num2)
opr(a,b)

print()

a=int(input("Enter 1st no = "))
b=int(input("2nd no = "))
c=int(input("3rd no = " ))
def maxi(num1,num2,num3):
	if(num1>=num2 and num1>=num3):
		return num1
	elif(num2>=num1 and num2>=num3):
		return num2
	else :
		return num3
print("Max = ",maxi(a,b,c))

print()


a = input("Enter n numbers : ")
l1 = a.split()
sum=0
i=0
while i < len(l1):
	sum = sum + int(l1[i])
	i = i+1
print("Sum = ",sum)

print()


a= input("Enter a string : ")
s=""
i=len(a)-1
while i >= 0:
	s= s+a[i]
	i = i-1
print(s)


print()


a=int(input("Enter a positive number = "))
count=0
i=1
while i <= a:
	if a%i == 0:
		count=count+1
	i=i+1
if count == 2:
	print(a," is a prime number.")
else:
	print(a," is not a prime number.")

print()

a= int(input("Enter a  number = "))
sum = 0
while(a!=0):
	d=a%10
	sum=sum*10+d
	a=a//10
print("reversed number :",sum)





print()




a=input("Enter a string : ")
l1=a.split()
i=0
s=""
while i<len(l1):
	b=l1[i]
	ss=""
	j=len(b)-1
	while j >= 0:
		ss = ss+b[j]
		j = j-1
	s =s+ ss + " "
	i = i+1
print("required string = ",s)


print()


num1= int(input("Enter greater number : "))
num2= int(input("Enter smaller number : "))
num3=num1%num2
while num3 != 0:
	num1=num2
	num2=num3
	num3=num1%num2
print("HCF = ",num2)
