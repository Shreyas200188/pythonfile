a=int(input("enter a number = "))
b=input("enter a binary number = ")
c=bin(a)
s2=str(c)
if ("0b"+b)==s2:
	print("Correct binary representation")
else:
	print("Incorrect binary representation")

print()


a=int(input("Enter a number : "))
s=""
while a>=1:
	d=a%2
	s=s+str(d)
	a=a//2
i=len(s)-1
s2=""
while i >= 0:
	s2= s2+s[i]
	i=i-1
print("Binary =",s2)
