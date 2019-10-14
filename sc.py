rup = int(input("Enter any amount of rupees : "))
tth = rup//2000
rup= rup-tth*2000
fhu=rup//500
rup = rup-fhu*500
thu=rup//200
rup=rup-thu*200
ohu = rup//100
rup=rup-ohu*100
fi=rup//50
rup=rup-fi*50
tw=rup//20
rup=rup-tw*20
te=rup//10
rup=rup-te*10
five=rup//5
rup=rup-five*5
two=rup//2
rup-=two*2


print("two thousand = ",tth)
print("five hundred = ",fhu)
print("two hundred = ",thu)
print("one hundred = ",ohu)
print("fifty = ",fi)
print("twenty = ",tw)
print("ten = ",te)
print("five = ",five)
print("two = ",two)
print("one = ",rup)


