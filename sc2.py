list1 = [10,10.1,30.4,'yolo']
a = 0
sum = 0
while(a<len(list1)) :
	if(type(list1[a]) == int or type(list1[a]) == float) :
		sum = sum + list1[a]
	a = a + 1
print(list1)
print("Summation = ",sum)



print()



list2 = ['aba','abc','1221','aa','a']
a=0
count = 0
while( a < len(list2)) :
	if(type(list2[a]) == str) :
		if(len(list2[a]) >= 2) :
			if(list2[a][0] == list2[a][len(list2[a])-1]):
				count = count + 1
	a = a+1
print(list2)
print("no of strings with req condition = ",count)


print()



list3 = [10,20,'aa',30,30,40,'aa',10.5,10.5,10]
print("Given list = ",list3)
a= 0
x=''
while(a<len(list3)):
	x=list3[a]
	m=a+1
	while(m<len(list3)) :
		if(list3[m] == x) :
			del list3[m]
		m = m+1
	a = a+1
print("Req list = ",list3)


print()




list4 = [20,30.6,'aa','bo',10,'yo']
list5=[20,40.5,'ab','lo','yo']
print("First list = ",list4)
print("Second list = ",list5)
a= 0
b= 0
while(a<len(list4)):
	x=list4[a]
	if ( x in list5):
		print("True ",x," exists in both lists")
	a=a+1


print()



list6 = [20,'sdbh',15,99,12,'lol',88.88]
print("Given list = ",list6)
a=0
while a < len(list6) :
	if(type(list6[a]) == int):
		if(list6[a] % 2 == 0):
			del list6[a]
	a=a+1 
print("Req list = ",list6)


print()


list7 = [1,2,3,4,3,2,1]
print("Given list = ",list7)
if(list7[0]==list7[len(list7)-1]):
	print("Given list is circularly identical")


print()

a="frwj  nfk"
v=a.split()
print(v)


print()


list8 = [1,2,3,1,2]
print("Given list = ",list8)
a=0
count = 0
while(a<len(list8)):
	x=list8[a]
	m=0
	while(m<len(list8)):
		if(list8[m]==list8[a]):
			count = count + 1
		m=m+1
	if(count == 1):
		print("Unique value = ",list8[a])
	count = 0
	a+=1

print()


a=input("Enter any number of words = ")
l=[]
l= a.split()
x= 0
while x <len(l):
	y = l[x]
	z=0
	while(z<len(l[x])):
		if(l[x][z:z+2]=='vi'):
			print("vi exists in the ",x+1,"th word, in the ",z+1,"th position.")
		z=z+1
	x=x+1


